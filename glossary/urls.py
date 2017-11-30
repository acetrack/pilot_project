from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^append$', views.append, name='append'),
    url(r'^appendArticle$', views.appendArticle, name='appendArticle'),
    # url(r'^glossary/hide', 'hide'),
    # url(r'^glossary/show', 'show'),
    # url(r'^glossary/list$', 'list'),
    # url(r'^glossary/clear$', 'clear'),
    # url(r'^glossary/hidden_list$', 'hidden_list'),
    # url(r'^glossary/new_list$', 'new_list'),
    #
    # url(r'^glossary$', 'my_glossary'),
    # url(r'^glossary/memory$', 'memory'),
    # url(r'^glossary/session$', 'session'),
    # url(r'^glossary/logout$', 'logout_session'),
]
