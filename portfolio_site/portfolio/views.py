from django.shortcuts import render
from portfolio.models import HomepageImages

def homepage(request):
    images = HomepageImages.objects.all()
    context = {
        'dict':images
    }
    return render(request, "index.html", context)

def projects(request):
    return render(request, "projects-compact-grid.html")
