from django.conf.urls import include, url
from django.contrib import admin


# App Urls
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^ems/', include('ems.urls')),
]


# Django Urls
urlpatterns += [
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
