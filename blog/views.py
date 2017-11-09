from django.shortcuts import render


def home(request):
    """
    Home page for blog.

    Parameters
    ----------
    request: object
        Django HttpRequest.

    Returns
    -------
    object: object
        Django HttpResponse.

    """
    template = 'blog/home.html'
    context = {}

    return render(request, template, context)
