from django.shortcuts import render
import os
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
import random


def index(request):
    avatars = [av for av in os.listdir(settings.STATIC_ROOT + os.sep + 'img' + os.sep + 'avatar')]
    temp = 'img' + os.sep + 'avatar' + os.sep + random.choice(avatars)
    avatar_img = static(temp)
    context = {'avatar_img': avatar_img}
    # context = {}
    template = "welcome.html"
    return render(request, template, context)
