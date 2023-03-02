from rest_framework import serializers
from coursemanagement.models import Course, Collection, Quiz, Question, QuizTaker



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'author', 'description', 'created_at', 'updated_at')

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'collection_name', 'author', 'courses')   

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'description', 'courses', 'time_limit')  

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'quiz', 'question_text', 'question_type')  

class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ('id','quiz', 'student', 'score', 'completed')      
        
             