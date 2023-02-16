from rest_framework import serializers
from coursemanagement.models import Course, Collection


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'author', 'description', 'created_at', 'updated_at')

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'collection_name', 'author', 'courses')   
        
             