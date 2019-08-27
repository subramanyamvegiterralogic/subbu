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
from testapp.api import views as api_view
from testapp.views import EmployeeListCreateModelMixin, EmployeeRetriveUpdateDestroyModelMixin , getEmployeeDetails,EmployeePostPerformsGet
from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('api',api_view.EmployeeDBClassBasedView,base_name='api')
from rest_framework.authtoken import views as rest_fw_view
from testapp2 import urls as testapp2_urls
from class_based_views import urls as testapp3_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp2/',include(testapp2_urls)),
    path('testapp3/',include(testapp3_urls)),
    # url(r'',include(router.urls)),

    url(r'^api/$',EmployeeListCreateModelMixin.as_view()),
    url(r'^api/?<pk>\d$',EmployeeRetriveUpdateDestroyModelMixin.as_view()),
    url(r'^locapi/<pk>\d$',getEmployeeDetails),
    url(r'^postapi/',EmployeePostPerformsGet.as_view()),
    url(r'^sqlite_postapi',api_view.EmployeeDBClassBasedView.as_view({"get": "retrieve", "post": "create", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="ticket-detail"),

]
