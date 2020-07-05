from django.shortcuts import render
from portfolio.models import HomepageImages, Gallery

def homepage(request):
    images = HomepageImages.objects.all()
    context = {
        'dict':images
    }
    return render(request, "index.html", context)

def projects(request):
    images = Gallery.objects.all()
    context = {
        'dict':images
    }
    return render(request, "projects-compact-grid.html", context)

def cv(request):
    return render(request, "cv.html")
