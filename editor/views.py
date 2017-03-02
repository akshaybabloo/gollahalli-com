from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

from .models import ContentModel
from .forms import ContentFormModel
import json
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
        return HttpResponseServerError

    if request.method == 'POST':
        form = ContentFormModel(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data.get('content')
            new_content, created = ContentModel.objects.update_or_create(ref_id='1')
            new_content.content = form_data
            new_content.save()

            return HttpResponseRedirect('/editor')
    else:
        form = ContentFormModel()

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
