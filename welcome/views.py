from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    template = "welcome.html"
    return render(request, template, context)
