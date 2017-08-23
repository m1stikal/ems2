from rest_framework import serializers
from ems.models import Vehicle

class VehSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('Veh_ID','Veh_Lat', 'Veh_Long')
