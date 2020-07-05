from django.db import models

class HomepageImages(models.Model):
    worked_for = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField()

class Gallery(models.Model):
    worked_for = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    main_image = models.ImageField()

class HireForm(models.Model):
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    description = models.CharField(max_length=1000)
