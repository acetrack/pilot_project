# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0002_auto_20171209_0857'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFileModel',
        ),
    ]