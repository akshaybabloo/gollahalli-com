from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import ProgrammingError
from django.forms.models import model_to_dict

from .models import ContentModel
from .forms import ContentFormModel
from utility import format_date_time


# ============================================================================================
#                                       Form Main
# ============================================================================================


@login_required
def index(request):
    template = "editor/home.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/admin/editor/contentmodel/add/')
    except ProgrammingError:
        return HttpResponseRedirect('/admin/editor/contentmodel/add/')

    if request.method == 'POST':
        form = ContentFormModel(request.POST)
        print(form)
        if form.is_valid():
            form_data = form.cleaned_data.items()
            form_data_dict = dict(form_data)
            new_content, created = ContentModel.objects.update_or_create(ref_id='1')

            new_content.cv = form_data_dict['cv']
            new_content.bio = form_data_dict['bio']
            new_content.url = form_data_dict['url']
            new_content.first_name = form_data_dict['first_name']
            new_content.last_name = form_data_dict['last_name']
            new_content.email_id = form_data_dict['email_id']
            new_content.github = form_data_dict['github']
            new_content.twitter = form_data_dict['twitter']
            new_content.linkedin = form_data_dict['linkedin']
            new_content.education_json = form_data_dict['education_json']
            new_content.experience_json = form_data_dict['experience_json']
            new_content.publication_json = form_data_dict['publication_json']
            new_content.research_area_json = form_data_dict['research_area_json']
            new_content.skills_t1_json = form_data_dict['skills_t1_json']
            new_content.skills_t2_json = form_data_dict['skills_t2_json']
            new_content.projects_json = form_data_dict['projects_json']
            new_content.tutorials_json = form_data_dict['tutorials_json']

            new_content.save()

            return HttpResponseRedirect('/editor')
    else:
        form = ContentFormModel(initial=model_to_dict(content))

    context = {'content': content, 'form': form,
               'created': format_date_time(content.created),
               'updated': format_date_time(content.updated),
               'website_name': content.website_name}
    return render(request, template, context)


def login(request):
    context = {}
    template = "editor/login.html"
    return render(request, template, context)


def log_out(request):
    logout(request)
    return redirect('index')
