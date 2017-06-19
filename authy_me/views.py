from django.contrib.auth.models import (User)
from django.shortcuts import render
from django.views.decorators.cache import never_cache


@never_cache
def users_js(request):
    """
        Returns a `user` JavaScript for Authenticator model.

        Parameters
        ----------
        request: WSGIRequest
            WSGI request.

        Returns
        -------
        render: HttpResponse
            Returns renderer's.

        """
    template = 'js/users.js'

    users = User.objects.all()

    context = {'users': users}

    return render(request, template, context, content_type='text/javascript')
