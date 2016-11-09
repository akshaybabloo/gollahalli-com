from django.shortcuts import render


def index(request):
    context = {}
    template = "index.html"
    return render(request, template, context)
