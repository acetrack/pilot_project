from django.urls import path
from . import views

app_name = 'glossary'
urlpatterns = [
    path('', views.to_remember_list, name='home'),
    path('append', views.append, name='append'),
    path('append_article', views.append_article, name='append_article'),
    path('append_url', views.append_url, name='append_url'),
    path('append_image', views.append_image, name='append_image'),
    path('append_document', views.append_document, name='append_document'),
    path('to_remember_list', views.to_remember_list, name='to_remember_list'),
    path('new_list', views.new_list, name='new_list'),
    path('hide', views.hide, name='hide'),
    path('show', views.show, name='show'),
    path('remembered_list', views.remembered_list, name='remembered_list'),
    path('memory', views.memory, name='memory'),
    path('delete_all', views.delete_all, name='delete_all'),
    path('delete_word', views.delete_word, name='delete_word'),
]
