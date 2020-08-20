from django.urls import include, path
from . import views

app_name = 'account'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign_up/', views.sign_up, name='sign_up'),
]