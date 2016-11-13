from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from gollahalli_me.settings import SHARE_URL
from editor.models import ContentModel


def index(request):
    context = {}
    template = "home.html"
    try:
        a = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist as e:
        return render(request, template, context)
    return render(request, template, context)


def page_not_found(request):
    url = request.get_full_path()
    img = static('img/404.png')
    home = SHARE_URL
    template = "error.html"
    context = {"url": SHARE_URL + url, "error": 404, "error_text": "Page not found.", "img": img, "home": home}
    return render(request, template, context)


def server_error(request):
    url = request.get_full_path()
    home = SHARE_URL
    img = static('img/500.png')
    template = "error.html"
    context = {"url": SHARE_URL + url, "error": 500, "error_text": "Sorry, but the requested page is unavailable due to a server hiccup.", "img": img, "home": home}
    return render(request, template, context)
