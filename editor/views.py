from django.shortcuts import render
from editor.models import ContentModel
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    context = {}
    template = "editor/home.html"
    try:
        a = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist as e:
        return render(request, template, context)
    except ObjectDoesNotExist as e:
        return render(request, template, context)
    return render(request, template, context)


def login(request):
    context = {}
    template = "editor/login.html"
    return render(request, template, context)
