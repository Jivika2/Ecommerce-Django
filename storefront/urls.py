"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
#import debug_toolbar

from django.conf import settings
from django.conf.urls import include

admin.site.site_header='Storefront Header'
admin.site.index_title='JK'
if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/',include('store.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    # Your other URL patterns...
    path('__debug__/', include(debug_toolbar.urls)),
]
