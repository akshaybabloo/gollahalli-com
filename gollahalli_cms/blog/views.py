from django.shortcuts import render, get_object_or_404

from gollahalli_cms.blog.models import PostModel


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


def post_list(request):
    post = PostModel.published.all()
    return render(request, 'blog/post/list.html', {'posts': post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(PostModel, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})
