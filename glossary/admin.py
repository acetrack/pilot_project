from django.contrib import admin
from .models import Glossary


class MyGlosarry(admin.ModelAdmin):
    list_display = ('word', 'frequency', 'account', 'glossary_title')


admin.site.register(Glossary, MyGlosarry)
