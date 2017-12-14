from django.contrib import admin
from .models import Glossary


# 이곳에 코드를 넣으면 admin에서 table을 볼 때 여기서 정리한 대로 보여준다
class MyGlosarry(admin.ModelAdmin):
    list_display = ('word', 'frequency', 'account', 'glossary_title')


admin.site.register(Glossary, MyGlosarry)
