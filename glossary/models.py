from django.db import models
from django.contrib.auth.models import User


class Glossary(models.Model):
    word = models.CharField(max_length=200)
    frequency = models.IntegerField()
    isShow = models.BooleanField()
    desc = models.CharField(max_length=500)
    isNew = models.BooleanField()
    account = models.ForeignKey(User)

    def __unicode__(self):
        return self.word

    def is_show_flag(self):
        return self.isShow


class UploadFileModel(models.Model):
    file = models.FileField(null=True)
