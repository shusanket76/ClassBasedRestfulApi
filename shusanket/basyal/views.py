
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializers
from .models import Student

class StudentApi(APIView):
    def get(self, request, pk = None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializers = StudentSerializers(stu)
            return Response(serializers.data)
        
        stu = Student.objects.all()
        serializers = StudentSerializers(stu, many=True)
        return Response(serializers.data)
    
    
    def post(self,request,format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("YOU DATA HAS BEEN SAVED")
        
        return Response(serializer.errors)
    
    
    def put(self, request, pk, format=None):
        stu= Student.objects.get(pk=pk)
        serizalier = StudentSerializers(stu, data= request.data)
        if serizalier.is_valid():
            serizalier.save()
            return Response("YOUR DATA HAS BEEN UPDATED")
        
        return Response(serizalier.errors)        
        
        
        
        
        
    
    
    def patch(self, request, pk , format=None):
        stu= Student.objects.get(pk=pk)
        serizalier = StudentSerializers(stu, data= request.data, partial=True)
        if serizalier.is_valid():
            serizalier.save()
            return Response("YOUR DATA HAS BEEN UPDATED")
        
        return Response(serizalier.errors)        
        
        
    def delete(self, request, pk, format= None):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        
        return Response("YOUR DATA HAS BEEN DELETED")
        
        
        
        
        
        