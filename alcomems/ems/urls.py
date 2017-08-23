from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'vehicles', views.VehicleViewSet, base_name='vehicles')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
