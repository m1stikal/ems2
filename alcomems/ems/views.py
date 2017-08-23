from django.shortcuts import render
from rest_framework import generics, viewsets, status
from ems.serializers import VehSerializer
from ems.models import Vehicle
from rest_framework.response import Response
from rest_framework.views import APIView
#from django.contrib.auth.models import permission
# Create your views here.


from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("Main View files for ems, get inspiration from webems")
'''
class VehList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehSerializer
    
class VehDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehSerializer
    
class UpdateVeh(APIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehSerializer
    def post(self, request, format=None):
        serializer = VehSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    '''def update(self, request, *args, **kwargs):
        serializer = VehSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)'''
