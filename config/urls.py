"""makeglossary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_page
# from account.views import sign_up

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^glossary/', include('glossary.urls', namespace='glossary')),
    url(r'^account/', include('account.urls', namespace='account')),

    # url(r'^login/$', auth_views.login, name='login',
    #     kwargs={'template_name': 'accounts/login.html', 'authentication_form': LoginForm}),
    # url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': 'index'}),



    # url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),
    # url(r'^mybook/$', views.mybook, name='mybook'),
]