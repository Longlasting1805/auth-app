from django.shortcuts import render
from .models import Course, Collection, Quiz, Question, QuizTaker, Answer, Assignment, Submission
from .serializers import CourseSerializer, CollectionSerializer, QuizSerializer, QuestionSerializer, QuizTakerSerializer, AnswerSerializer, AssignmentSerializer, SubmissionSerializer
from rest_framework.views import APIView
from django.db.models import F 
from rest_framework.response import Response
from rest_framework import permissions


# Create your views here.

class CourseView(APIView):
      def get_permissions(self):
          if self.request.method == ['POST', 'PUT', 'DELETE']:
             return [permissions.IsAdminUser,]
          
          elif self.request.method == 'GET':
               return [permissions.AllowAny(),]  
          else:
              return []
          
      def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


      def get(self, request):
          courses = Course.objects.all()
          serializer = CourseSerializer(courses, many=True)
          return Response(serializer.data)
      
      def put(self, request, pk):
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
            else:
               return Response(serializer.errors, status=400)
      
      def delete(self, request, pk):
          course = Course.objects.get(pk=pk)
          course.delete()
          return Response(status=204)


class CollectionView(APIView):
      permission_classes = [permissions.AllowAny]
     
      def post(self, request):
          collection = Collection.objects.get_or_create(user=request.user)
          course = Course.objects.get(pk=request.data['course_id'])
          collection.courses.add(course)  
          serializer = CollectionSerializer(collection)
          return Response(serializer.data, status=201)
      
      def delete(self, request):
          collection = Collection.objects.get_or_create(user=request.user)
          course = Course.objects.get(pk=request.data['course_id'])
          collection.courses.delete(course) 
          serializer = CollectionSerializer(collection) 
          return Response(serializer.data, status=204)
          
 

# class ListQuizView(generics.ListAPIView):
#         queryset = Quiz.objects.all()
#         serializer_class = QuizSerializer

# class DetailQuizView(generics.UpdateAPIView):
#         queryset = Quiz.objects.all()
#         serializer_class = QuizSerializer  

# class ListQuestionView(generics.ListAPIView):
#         queryset = Question.objects.all()
#         serializer_class = QuestionSerializer

# class DetailQuestionView(generics.UpdateAPIView):
#         queryset = Question.objects.all()
#         serializer_class = QuestionSerializer 


# class ListQuizTakerView(generics.ListAPIView):
#         queryset = QuizTaker.objects.all()
#         serializer_class = QuizTakerSerializer

# class DetailQuizTakerView(generics.UpdateAPIView):
#         queryset = QuizTaker.objects.all()
#         serializer_class = QuizTakerSerializer        

# class ListAnswerView(generics.ListAPIView):
#         queryset = Answer.objects.all()
#         serializer_class = AnswerSerializer

# class DetailAnswerView(generics.UpdateAPIView):
#         queryset = Answer.objects.all()
#         serializer_class = AnswerSerializer  

# class ListAssignmentView(generics.ListAPIView):
#         queryset = Assignment.objects.all()
#         serializer_class = AssignmentSerializer

# class DetailAssignmentView(generics.UpdateAPIView):
#         queryset = Assignment.objects.all()
#         serializer_class = AssignmentSerializer 

# class ListSubmissionView(generics.ListAPIView):
#         queryset = Submission.objects.all()
#         serializer_class = SubmissionSerializer

# class DetailSubmissionView(generics.UpdateAPIView):
#         queryset = Submission.objects.all()
#         serializer_class = SubmissionSerializer                                          





       
        
    
