# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gardeners', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='following',
            old_name='Following',
            new_name='following',
        ),
    ]
