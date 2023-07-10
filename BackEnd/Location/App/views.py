# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from App.models import Location
# from rest_framework import serializers
# from rest_framework import status
from App.serialize import LocationSerializer

# Create your views here.

def home(request):
    return HttpResponse("hello")



class LocationAdd(APIView):
    def post(self,request):
        LocationObj = LocationSerializer(data=request.data)
        if LocationObj.is_valid():
            LocationObj.save()
            return Response(200)
        return Response(LocationObj.errors)
    

class LocationShow(APIView):
    def get(self,request):
        LocationObj = Location.objects.all()
        Serialise = LocationSerializer(LocationObj,many=True)
        return Response(Serialise.data)

class LocationUpdate(APIView):
    def post(self,request,pk):
        try:
            UpdateObj = Location.objects.get(pk=pk)
        except:
            return Response("Error in Database")
        
        LocationObj = LocationSerializer(UpdateObj,data=request.data)
        if LocationObj.is_valid():
            LocationObj.save()
            return Response(200)
        return Response(LocationObj.errors)
    

class LocationDelete(APIView):
    def post(self,request,pk):
        try:
            DeleteObj = Location.objects.get(pk=pk)
        except:
            return Response("Error in Database")
        DeleteObj.delete()
        return Response(200)
        return Response(LocationObj.errors)

