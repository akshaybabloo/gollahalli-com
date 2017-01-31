from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect

from .models import ContentModel
from .forms import ContentFormModel
import utility

# ============================================================================================
#                                       Form Main
# ============================================================================================


@login_required
def index(request):
    template = "editor/home.html"

    try:
        json_content = ContentModel.objects.get(ref_id='1')
    except Exception:
        raise HttpResponseServerError

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

    context = {'content': json_content.content, 'form': form}
    return render(request, template, context)


def login(request):
    context = {}
    template = "editor/login.html"
    return render(request, template, context)


def log_out(request):
    logout(request)
    return redirect('index')
