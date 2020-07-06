from django.shortcuts import render
from portfolio.models import HomepageImages, Gallery, ProfilePic
from django.views.generic import TemplateView, ListView, DetailView, View
from portfolio.models import HireForm

def homepage(request):
    images = HomepageImages.objects.all()
    profile_object = ProfilePic.objects.get(use_me_as_profile=True)
    context = {
        'dict':images,
        'profile_object':profile_object,
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

def hire_me(request):
    return render(request, "hire-me.html")

class HireMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, "hire-me.html")

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = request.POST
            entry = HireForm(
                phone=form.get('phone'),
                email=form.get('email'),
                description=form.get('message')
            )
            print(form.get('message'))
            entry.save()

        return render(request, "index.html")
