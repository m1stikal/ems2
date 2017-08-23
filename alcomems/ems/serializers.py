from django.contrib.auth.models import User
from rest_framework import serializers
import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = ('Veh_ID','Veh_Lat', 'Veh_Long')
