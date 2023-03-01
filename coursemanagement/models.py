from django.db import models
from accounts.models import *

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(UserData, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Collection(models.Model):
    author = models.ForeignKey(UserData, on_delete=models.SET_NULL, null=True)
    collection_name = models.CharField(max_length=200, null=True )
    courses = models.ManyToManyField(Course, help_text='select a course for this collection')    

    def __str__(self):
        return self.collection_name

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #        Collection.objects.filter(pk=self.courses).update(courses_count=F('courses_count')+1)
    #     super().save(*args, **kwargs)    

    

class Quiz(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    courses = models.ForeignKey(Course, on_delete=models.CASCADE,  null=True)
    time_limit = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
       
    def __str__(self):
        return self.title

QUESTION_TYPE = (
    ('single', 'single'),
    ('multiple', 'multiple'),
)        

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200, choices=QUESTION_TYPE, default='single')

    def __str__(self):
        return self.question_text

class QuizTaker(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True)
    score = models.FloatField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.quiz
