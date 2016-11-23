import os
import random

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render

from .forms import WelcomeFormModel
from .models import AbiesModel


def index(request):
    if request.method == 'POST':
        form = WelcomeFormModel(request.POST, request.FILES)
        if form.is_valid():
            firs_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            company_name = form.cleaned_data['company_name']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']

            profile_image_location = request.FILES.get('profile_image_location', None)
            company_logo_location = request.FILES.get('company_logo_location', None)

            if profile_image_location is not None:
                newdoc = AbiesModel(welcome_profile_image_location=request.FILES['profile_image_location'])
                newdoc.save()
            if company_logo_location is not None:
                newdoc = AbiesModel(welcome_profile_image_location=request.FILES['company_logo_location'])
                newdoc.save()
            print(firs_name, last_name, email, username, company_name, city, country)
        else:
            print('not valid')
    else:
        form = WelcomeFormModel()

    avatars = [av for av in os.listdir(settings.STATIC_ROOT + os.sep + 'img' + os.sep + 'avatar')]
    random_image_location = 'img' + os.sep + 'avatar' + os.sep + random.choice(avatars)
    avatar_img = static(random_image_location)
    template = "welcome.html"
    context = {'avatar_img': avatar_img, 'form': form}
    return render(request, template, context)
