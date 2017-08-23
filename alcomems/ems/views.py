from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
import serializers
import models


class ReadOnlyPermission(permissions.BasePermission):
    """
    Permission used for readonly endpoints.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated, ReadOnlyPermission,)
    queryset = User.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VehicleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Vehicle.objects.all()
