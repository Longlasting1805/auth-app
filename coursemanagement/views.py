from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Course, Collection
from .serializers import CourseSerializer, CollectionSerializer
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import F 
from rest_framework.response import Response
from rest_framework import permissions
from accounts.models import UserData
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework import status



# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated) 

    def post(self, request, *args, **kwargs):

        if not request.user.is_staff:
            return Response({'error': 'Only admin users can create courses.'}, status=status.HTTP_403_FORBIDDEN)

        return super().create(request, *args, **kwargs)

    # def get_permissions(self):
    #     if self.request.method == ['POST', 'PUT', 'DELETE']:
    #         return [permissions.IsAdminUser,]
        
    #     elif self.request.method == 'GET':
    #         return [permissions.AllowAny(),]  
    #     else:
    #         return []
    
    # @action(permission_classes=[permissions.IsAdminUser], detail=False, url_name='creates', url_path='creates', methods=['post'])
    # def creates(self, request, *args, **kwargs):
        # print(request.data.get('user'))

        # if (request.data.get('user') == 2):

        #     return Response('error')

        # serializer = CourseSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=201)
        # else:
        #     return Response(serializer.errors, status=400)

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def get(self, request):
    #     courses = Course.objects.all()
    #     serializer = CourseSerializer(courses, many=True)
    #     return Response(serializer.data)
    
    # def put(self, request, pk):
    #     course = Course.objects.get(pk=pk)
    #     serializer = CourseSerializer(course, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)
    
    # def delete(self, request, pk):
    #     course = Course.objects.get(pk=pk)
    #     course.delete()
    #     return Response(status=204)


class CollectionViewset(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [permissions.AllowAny]

    @login_required
    def add_course(request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        Collection.objects.get_or_create(user=request.user, course=course)
        return HttpResponseRedirect(reverse('my_collection'))

    @login_required
    def remove_course(request, course_id):
        collection = get_object_or_404(Collection, user=request.user, course_id=course_id)
        collection.delete()
        return HttpResponseRedirect(reverse('my_collection'))

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     email = request.user.email
    #     if not UserData.objects.filter(email= email).exists:
    #             return Response({'detail': "User does not exist"})
    #     serializer = CollectionSerializer(request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save
    #     return Response(serializer.data, status=201)
        # collection = Collection.objects.get_or_create(**request.data, user=email)
        # course = Course.objects.get(pk=request.data['course_id'])
        # collection.courses.add(course)  
        # serializer = CollectionSerializer(collection)
        # return Response(serializer.data, status=201)
        
    #   def post(self, request):
    #       print(request.data)
    #       email = request.user
    #       print(email)
    #       if not UserData.objects.filter(email= email).exists:
    #           return Response({'detail': "User does not exist"})
    #       collection = Collection.objects.get_or_create(**request.data, user=email)
    #       course = Course.objects.get(pk=request.data['course_id'])
    #       collection.courses.add(course)  
    #       serializer = CollectionSerializer(collection)
    #       return Response(serializer.data, status=201)
      
    # def delete(self, request):
    #     collection = Collection.objects.get_or_create(user=request.user)
    #     course = Course.objects.get(pk=request.data['course_id'])
    #     collection.courses.delete(course) 
    #     serializer = CollectionSerializer(collection) 
    #     return Response(serializer.data, status=204)
          
 

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

