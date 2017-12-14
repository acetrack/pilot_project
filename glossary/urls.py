from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.to_remember_list, name='home'),
    url(r'^append$', views.append, name='append'),
    url(r'^append_article$', views.append_article, name='append_article'),
    url(r'^append_url$', views.append_url, name='append_url'),
    url(r'^append_image$', views.append_image, name='append_image'),
    url(r'^append_document$', views.append_document, name='append_document'),
    url(r'^to_remember_list$', views.to_remember_list, name='to_remember_list'),
    url(r'^new_list$', views.new_list, name='new_list'),
    url(r'^hide', views.hide, name='hide'),
    url(r'^show', views.show, name='show'),
    url(r'^remembered_list$', views.remembered_list, name='remembered_list'),
    url(r'^memory$', views.memory, name='memory'),
    url(r'^delete_all', views.delete_all, name='delete_all'),
    url(r'^delete_word', views.delete_word, name='delete_word'),
    # url(r'^glossary/clear$', 'clear'),
    # url(r'^glossary/hidden_list$', 'hidden_list'),
    # url(r'^glossary/new_list$', 'new_list'),
    #
    # url(r'^glossary$', 'my_glossary'),
    # url(r'^glossary/memory$', 'memory'),
    # url(r'^glossary/session$', 'session'),
    # url(r'^glossary/logout$', 'logout_session'),
]
