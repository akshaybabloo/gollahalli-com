from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

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
        json_content = ContentModel.objects.get(ref_id='1')
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

    context = {'content': json.dumps(json_content.content), 'form': form,
               'updated': format_date_time(json_content.updated),
               'website_name': json_content.website_name}
    return render(request, template, context)


def login(request):
    context = {}
    template = "editor/login.html"
    return render(request, template, context)


def log_out(request):
    logout(request)
    return redirect('index')
