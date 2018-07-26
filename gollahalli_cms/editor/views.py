from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from editor.forms import ContentModelForm, MetaContentModelForm, EducationContentModelForm, ProjectContentModelForm, \
    TutorialContentModelForm, ExperienceContentModelForm
from editor.models import ContentModel, MetaContentModel


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

    template = "portal/editor/content/editor_content_form_index.html"

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
    template = "portal/editor/education/editor_education_form_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False
        return redirect('content_home')

    form_msg = ''

    if request.method == 'POST':
        form = EducationContentModelForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('website_name')
            from_date = form.cleaned_data.get('from_date')
            to_date = form.cleaned_data.get('to_date')
            where = form.cleaned_data.get('where')
            current = form.cleaned_data.get('current')
            file = form.cleaned_data.get('file')
            image = form.cleaned_data.get('image')

            education_model, created = content.education.update_or_create(ref_id=1, title=title, from_date=from_date,
                                                                          to_date=to_date, where=where, current=current,
                                                                          file=file, image=image)

            if created:
                education_model.save()
                form_msg = "Updates saved"
                content = education_model
    else:
        form = EducationContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)


@login_required()
def projects_content(request):
    template = "portal/editor/project/project_content_form_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False
        return redirect('content_home')

    form_msg = ''

    if request.method == 'POST':
        form = ProjectContentModelForm(request.POST)

        if form.is_valid():
            link = form.cleaned_data.get('link')
            title = form.cleaned_data.get('title')
            long_description = form.cleaned_data.get('long_description')
            file = form.cleaned_data.get('file')
            image = form.cleaned_data.get('image')

            project_model, created = content.projects.update_or_create(ref_id=1, link=link, title=title,
                                                                       long_description=long_description,
                                                                       file=file, image=image)

            if created:
                project_model.save()
                form_msg = "Updates saved"
                content = project_model
    else:
        form = ProjectContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)


@login_required()
def tutorials_content(request):
    template = "portal/editor/tutorial/tutorial_content_form_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False
        return redirect('content_home')

    form_msg = ''

    if request.method == 'POST':
        form = TutorialContentModelForm(request.POST)

        if form.is_valid():
            link = form.cleaned_data.get('link')
            title = form.cleaned_data.get('title')
            long_description = form.cleaned_data.get('long_description')
            file = form.cleaned_data.get('file')
            image = form.cleaned_data.get('image')

            tutorial_model, created = content.tutorials.update_or_create(ref_id=1, link=link, title=title,
                                                                         long_description=long_description,
                                                                         file=file, image=image)

            if created:
                tutorial_model.save()
                form_msg = "Updates saved"
                content = tutorial_model
    else:
        form = TutorialContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)


@login_required()
def experience_content(request):
    template = "portal/editor/experience/experience_content_form_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False
        return redirect('content_home')

    form_msg = ''

    if request.method == 'POST':
        form = ExperienceContentModelForm(request.POST)

        if form.is_valid():

            from_date = form.cleaned_data.get('from_date')
            to_date = form.cleaned_data.get('to_date')
            title = form.cleaned_data.get('title')
            where_city = form.cleaned_data.get('where_city')
            where_country = form.cleaned_data.get('where_country')
            company = form.cleaned_data.get('company')
            current = form.cleaned_data.get('current')

            experience_model, created = content.experience.update_or_create(ref_id=1, title=title, from_date=from_date,
                                                                            to_date=to_date, where_city=where_city,
                                                                            where_country=where_country,
                                                                            current=current, company=company)

            if created:
                experience_model.save()
                form_msg = "Updates saved"
                content = experience_model
    else:
        form = ExperienceContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)


@login_required()
def skills_content(request):
    template = "portal/editor/education/editor_education_form_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False
        return redirect('content_home')

    form_msg = ''

    if request.method == 'POST':
        form = EducationContentModelForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('website_name')
            from_date = form.cleaned_data.get('website_name')
            to_date = form.cleaned_data.get('website_name')
            where = form.cleaned_data.get('website_name')
            current = form.cleaned_data.get('website_name')
            file = form.cleaned_data.get('website_name')
            image = form.cleaned_data.get('website_name')

            education_model, created = content.education.update_or_create(ref_id=1, title=title, from_date=from_date,
                                                                          to_date=to_date, where=where, current=current,
                                                                          file=file, image=image)

            if created:
                education_model.save()
                form_msg = "Updates saved"
                content = education_model
    else:
        form = ContentModelForm()

    context = {'form': form, 'content': content, 'form_msg': form_msg}

    return render(request, template, context)


@login_required()
def publications_content(request):
    template = "portal/editor/education/editor_education_form_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False
        return redirect('content_home')

    form_msg = ''

    if request.method == 'POST':
        form = EducationContentModelForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('website_name')
            from_date = form.cleaned_data.get('website_name')
            to_date = form.cleaned_data.get('website_name')
            where = form.cleaned_data.get('website_name')
            current = form.cleaned_data.get('website_name')
            file = form.cleaned_data.get('website_name')
            image = form.cleaned_data.get('website_name')

            education_model, created = content.education.update_or_create(ref_id=1, title=title, from_date=from_date,
                                                                          to_date=to_date, where=where, current=current,
                                                                          file=file, image=image)

            if created:
                education_model.save()
                form_msg = "Updates saved"
                content = education_model
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
    template = "portal/editor/meta/meta_content_form_index.html"

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
