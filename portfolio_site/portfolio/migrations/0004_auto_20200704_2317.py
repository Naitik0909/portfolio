# Generated by Django 3.0.7 on 2020-07-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200704_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='worked_for',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepageimages',
            name='worked_for',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
