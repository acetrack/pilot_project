# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='glossary',
            name='glossary_title',
            field=models.CharField(default='undefined', max_length=200),
        ),
    ]
