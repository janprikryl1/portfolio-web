"""portfolio_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import re_path
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve

from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),  # Odkaz na stránku admin, kde je přístup ke všem datům
    re_path(r'^', include("main.url")),  # Odkaz na hlavní aplikaci

    # Odkaz na soubory
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/media/icon/icon.svg')),
)
handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'




"""
V Django 3.8

urlpatterns = [
    url(r'^', include("main.url"))
] + i18n_patterns(
    path('admin/', admin.site.urls),  # Odkaz na stránku admin, kde je přístup ke všem datům
    url(r'^', include("main.url")),  # Odkaz na hlavní aplikaci

    # Odkaz na soubory
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/media/icon/icon.svg')),

)
handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
"""