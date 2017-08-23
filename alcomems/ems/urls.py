from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from ems import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^api/$', views.VehList.as_view()),
    url(r'^api/(?P<pk>[\w\-]+)/$', views.VehDetail.as_view()),
    url(r'^api2/(?P<pk>[\w\-]+)/$', views.UpdateVeh.as_view()),
]
#<pk>[0-9]
urlpatterns = format_suffix_patterns(urlpatterns)
