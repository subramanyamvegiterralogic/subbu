from django.conf.urls import url,include
from class_based_views import views as ta3_views

# Test Comment Added for testing purpose
# EOD Commoit on 2019-08-28
urlpatterns=[
    url(r'^api',ta3_views.EmployeeListCreateAPIView.as_view()),
    url(r'^api/(?P<id>\d)/$',ta3_views.EmployeeRetriveUpdatedestroyAPIView.as_view()),
    url(r'^api_mixin/(?P<id>\d)/$',ta3_views.EmployeeRetriveUpdateDestroyMixin.as_view()),
    # url(r'^get_data',ta2_views.get_data),
]
