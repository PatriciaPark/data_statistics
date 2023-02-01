"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from .views import *
from django.conf.urls import handler400, handler404, handler500

handler400 = 'django.views.defaults.bad_request'
handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('csd/', include('csd.urls')),
    path('csm/', include('csm.urls')),
    path('csy/', include('csy.urls')),
    path('csp/', include('csp.urls')),
    path('csr/', include('csr.urls')),
    path('store/', include('store.urls')),
    path('users/', include('users.urls')),
]

# urlpatterns.append(re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}))
# urlpatterns.append(re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}))
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)