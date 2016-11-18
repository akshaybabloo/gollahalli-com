from django.shortcuts import render, redirect
from django.conf import settings
from editor.models import ContentModel


def index(request):
    context = {}
    template = "viewer/home.html"
    try:
        a = ContentModel.objects.get(ref_id='1')
    except Exception as e:
        return redirect('/welcome/')
    return render(request, template, context)


def page_not_found(request):
    url = request.get_full_path()
    home_link = settings.SHARE_URL
    template = "error.html"
    context = {"url": home_link + url, "error_code": 404,
               "error_message": "Oops, the page you're <br/> looking for does not exist.", "home_link": home_link}
    return render(request, template, context)


def server_error(request):
    url = request.get_full_path()
    home_link = settings.SHARE_URL
    template = "error.html"
    context = {"url": home_link + url, "error_code": 500,
               "error_message": "Sorry, but the requested page is unavailable <br/> due to a server hiccup.",
               "home_link": home_link}
    return render(request, template, context)
