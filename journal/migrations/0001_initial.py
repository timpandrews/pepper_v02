# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('badge', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.TextField()),
                ('createTS', models.DateTimeField(auto_now_add=True)),
                ('updateTS', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
