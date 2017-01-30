from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect
from django.shortcuts import render

from editor.models import ContentModel


@login_required
def index(request):

    template = "editor/home.html"
    try:
        json_content = ContentModel.objects.get(ref_id='1')
    except Exception as e:
        raise HttpResponseServerError

    context = {'content': json_content.content}
    return render(request, template, context)


def login(request):
    context = {}
    template = "editor/login.html"
    return render(request, template, context)


def log_out(request):
    logout(request)
    return redirect('index')
