# Generated by Django 3.0.7 on 2020-07-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepageimages',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]