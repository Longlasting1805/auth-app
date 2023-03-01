from django.shortcuts import render
from .models import Course, Collection
from .serializers import CourseSerializer, CollectionSerializer
from rest_framework import generics
from django.db.models import F 
# from rest_framework.response import Response


# Create your views here.

class ListCourseView(generics.ListAPIView):
        queryset = Course.objects.all()
        serializer_class = CourseSerializer

class DetailCourseView(generics.RetrieveAPIView):
    queryset =Course.objects.all()
    serializer_class = CourseSerializer  

class ListCollectionView(generics.ListAPIView):
        queryset = Collection.objects.all()
        serializer_class = CollectionSerializer

class DetailCollectionView(generics.UpdateAPIView):
        queryset = Collection.objects.all()
        serializer_class = CollectionSerializer        




       
        
    
