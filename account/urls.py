from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
]