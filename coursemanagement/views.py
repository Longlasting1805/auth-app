from django.shortcuts import render
from .models import Course, Collection, Quiz, Question, QuizTaker, Answer, Assignment, Submission
from .serializers import CourseSerializer, CollectionSerializer, QuizSerializer, QuestionSerializer, QuizTakerSerializer, AnswerSerializer, AssignmentSerializer, SubmissionSerializer
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

class ListQuizView(generics.ListAPIView):
        queryset = Quiz.objects.all()
        serializer_class = QuizSerializer

class DetailQuizView(generics.UpdateAPIView):
        queryset = Quiz.objects.all()
        serializer_class = QuizSerializer  

class ListQuestionView(generics.ListAPIView):
        queryset = Question.objects.all()
        serializer_class = QuestionSerializer

class DetailQuestionView(generics.UpdateAPIView):
        queryset = Question.objects.all()
        serializer_class = QuestionSerializer 


class ListQuizTakerView(generics.ListAPIView):
        queryset = QuizTaker.objects.all()
        serializer_class = QuizTakerSerializer

class DetailQuizTakerView(generics.UpdateAPIView):
        queryset = QuizTaker.objects.all()
        serializer_class = QuizTakerSerializer        

class ListAnswerView(generics.ListAPIView):
        queryset = Answer.objects.all()
        serializer_class = AnswerSerializer

class DetailAnswerView(generics.UpdateAPIView):
        queryset = Answer.objects.all()
        serializer_class = AnswerSerializer  

class ListAssignmentView(generics.ListAPIView):
        queryset = Assignment.objects.all()
        serializer_class = AssignmentSerializer

class DetailAssignmentView(generics.UpdateAPIView):
        queryset = Assignment.objects.all()
        serializer_class = AssignmentSerializer 

class ListSubmissionView(generics.ListAPIView):
        queryset = Submission.objects.all()
        serializer_class = SubmissionSerializer

class DetailSubmissionView(generics.UpdateAPIView):
        queryset = Submission.objects.all()
        serializer_class = SubmissionSerializer                                          





       
        
    
