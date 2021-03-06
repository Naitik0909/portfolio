# Generated by Django 3.0.7 on 2020-07-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200704_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
