from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from home.views import home_page
from django.urls import include, path

urlpatterns = [
    path('', home_page, name='home'),
    # path('custom_sign_in', custom_sign_in, name='custom_sign_in'),
    path('admin/', admin.site.urls),
    path('glossary/', include('glossary.urls')),
    path('accounts/', include("allauth.urls")),
    # path('account/', include('account.urls')),
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
