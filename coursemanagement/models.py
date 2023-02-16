from django.db import models
from accounts.models import *

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(UserData, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Collection(models.Model):
    collection_name = models.CharField(max_length=200, null=True )
    author = models.ForeignKey(UserData, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(Course, help_text='select a course for this collection')    

    def __str__(self):
        return self.collection_name

        
