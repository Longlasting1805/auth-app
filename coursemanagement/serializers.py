from rest_framework import serializers
from coursemanagement.models import Course, Collection, Quiz, Question, QuizTaker, Answer, Assignment, Submission



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 
                'title', 
                'author', 
                'description', 
                'created_at', 
                'updated_at'
]
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 
                'collection_name', 
                'author', 
                'courses')   

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 
                'name', 
                'topic', 
                'number_of_questions',
                'courses', 
                'required_score_to_pass', 
                'time_limit')  

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 
                'quiz', 
                'question_text', 
                'question_type')  

class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ('id', 
                'quiz', 
                'student', 
                'score', 
                'completed') 

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id',
                'text',
                'correct',
                'question') 

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 
                'essay', 
                'description', 
                'student', 
                'schedule', 
                'deadline', 
                'grade')                
             
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id',
                'assignment',
                'student',
                'comment',
                'date')           
        
             