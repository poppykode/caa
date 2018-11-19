"""caa_web_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from _admin.views import DashboardView
from fees.paynow import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',DashboardView, name='home'),
    path('admin/',include('_admin.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('api/v1/library/',include('library.urls')),
    path('fees/',include('fees.urls')),
     
    #endpoints
    path('api/v1/', include('courses_grades.urls')),
    path('api/v1/clickers/',include('clickers.urls')),
    path('api/v1/accounts/',include('_user.urls')),

    path('paynow/initiate/', PayNowView.as_view(), name="paynow"),
    path('paynow/result/', ResultView.as_view(), name="result"),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
