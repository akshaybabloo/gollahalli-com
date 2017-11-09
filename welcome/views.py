from django.shortcuts import render


def home(request, register='new_registration'):
    """
    Welcome page for new setup.

    Parameters
    ----------
    request: object
        WSGI request.
    register: bool
        Defaults to False.

    Returns
    -------
    render: object
        Returns renderer's.

    """

    template = 'welcome/welcome.html'

    context = {'check_db_connection': False, 'check_ssl': False, 'check_users': False, 'check_authy': False,
               'check_smtp': False, 'check_aws': False, 'check_cloudinary': False}

    return render(request, template, context)
