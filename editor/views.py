from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import ProgrammingError
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect

from gollahalli_com.utils import format_date_time
from .forms import ContentFormModel
from .models import ContentModel


# ============================================================================================
#                                       Form Main
# ============================================================================================

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
    template = "portal/editor/editor_index.html"

    try:
        content = ContentModel.objects.get(ref_id='1')
    except ContentModel.DoesNotExist:
        content = False

    context = {'content': content}
    return render(request, template, context)

