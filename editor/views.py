from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ContentModelForm, MetaContentModelForm
from .models import ContentModel, MetaContentModel


# ============================================================================================
#                                       Form Main
# ============================================================================================
@login_required
def portal_home(request):
    """
    Portal Home page.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.
    """
    template = 'portal/portal_index.html'

    context = {}

    return render(request, template, context)


@login_required
def editor_home(request):
    """
    Editor home page.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.
    """
    template = "portal/editor/editor_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False

    context = {'content': content}
    return render(request, template, context)


@login_required
def content_home(request):
    """
    Editor content home page.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.
    """

    template = "portal/editor/editor_content_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False

    form_msg = ''

    if request.method == 'POST':
        form = ContentModelForm(request.POST)

        if form.is_valid():
            website_name = form.cleaned_data.get('website_name')
            cv = form.cleaned_data.get("cv")
            bio = form.cleaned_data.get("bio")
            url = form.cleaned_data.get("url")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email_id = form.cleaned_data.get("email_id")
            github = form.cleaned_data.get("github")
            twitter = form.cleaned_data.get("twitter")
            linkedin = form.cleaned_data.get("linkedin")
            file = form.cleaned_data.get("file")
            image = form.cleaned_data.get("image")

            content_model, created = ContentModel.objects.update_or_create(ref_id=1,
                                                                           website_name=website_name,
                                                                           cv=cv,
                                                                           bio=bio,
                                                                           url=url,
                                                                           first_name=first_name,
                                                                           last_name=last_name,
                                                                           email_id=email_id,
                                                                           github=github,
                                                                           twitter=twitter,
                                                                           linkedin=linkedin,
                                                                           file=file,
                                                                           image=image)

            if created:
                content_model.save()
                form_msg = "Updates saved"
                content = content_model
    else:
        form = ContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)


@login_required()
def education_content(request):
    template = "portal/editor/editor_education_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False

    form_msg = ''

    if request.method == 'POST':
        form = ContentModelForm(request.POST)

        if form.is_valid():
            website_name = form.cleaned_data.get('website_name')
            cv = form.cleaned_data.get("cv")
            bio = form.cleaned_data.get("bio")
            url = form.cleaned_data.get("url")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email_id = form.cleaned_data.get("email_id")
            github = form.cleaned_data.get("github")
            twitter = form.cleaned_data.get("twitter")
            linkedin = form.cleaned_data.get("linkedin")
            file = form.cleaned_data.get("file")
            image = form.cleaned_data.get("image")

            content_model, created = ContentModel.objects.update_or_create(ref_id=1,
                                                                           website_name=website_name,
                                                                           cv=cv,
                                                                           bio=bio,
                                                                           url=url,
                                                                           first_name=first_name,
                                                                           last_name=last_name,
                                                                           email_id=email_id,
                                                                           github=github,
                                                                           twitter=twitter,
                                                                           linkedin=linkedin,
                                                                           file=file,
                                                                           image=image)

            if created:
                content_model.save()
                form_msg = "Updates saved"
                content = content_model
    else:
        form = ContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)


@login_required
def meta_home(request):
    """
    Meta content home page.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.
    """
    template = "portal/editor/meta_content_index.html"

    try:
        content = MetaContentModel.objects.get(ref_id=1)
    except MetaContentModel.DoesNotExist:
        content = False

    form_msg = ''

    if request.method == "POST":
        form = MetaContentModelForm(request.POST)

        if form.is_valid():
            header = form.cleaned_data.get('header')
            footer = form.cleaned_data.get('footer')
            meta = form.cleaned_data.get('meta')

            content_model, created = MetaContentModel.objects.update_or_create(ref_id=1, header=header, footer=footer,
                                                                               meta=meta)

            if created:
                content_model.save()
                form_msg = "Updates saved"
                content = content_model
    else:
        form = MetaContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)
