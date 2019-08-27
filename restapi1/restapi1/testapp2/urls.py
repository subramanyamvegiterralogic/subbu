"""restapi1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from rest_framework.authtoken import views as rest_fw_view
from testapp2 import views as ta2_views
urlpatterns = [
    url(r'^emp/$',ta2_views.return_data),
    url(r'^get_data',ta2_views.get_data),
    url(r'^create_data',ta2_views.create_new_record),
    url(r'^put_data',ta2_views.put_details),
    url(r'^patch_data',ta2_views.patch_details),
    url(r'^delete_data/<id>\d$',ta2_views.delete_details),
]
