from django.db import models


class Vehicle(models.Model):
    Veh_ID = models.CharField(max_length=100, unique=True, primary_key=True)
    Agency = models.CharField(max_length=200)
    Available = models.BooleanField(default=True)
    Veh_Lat = models.DecimalField(max_digits=7, decimal_places=5, default=0)
    Veh_Long = models.DecimalField(max_digits=7, decimal_places=5, default=0)


class Dispatch(models.Model):
    Inc_ID = models.AutoField(unique=True, primary_key=True)
    Inc_date = models.DateTimeField('date of incident')
    Veh_ID = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    Veh_Miles_Begin = models.PositiveIntegerField(default=0)
    Veh_Miles_End = models.PositiveIntegerField(default=0)
    Inc_Lat = models.DecimalField(max_digits=7, decimal_places=5, default=0)
    Inc_Long = models.DecimalField(max_digits=7, decimal_places=5, default=0)

