from django.urls import path
from .views import ListCourseView, DetailCourseView, ListCollectionView, DetailCollectionView, ListQuizView, DetailQuizView, ListQuestionView, DetailQuestionView, ListQuizTakerView, DetailQuizTakerView, ListAnswerView, DetailAnswerView

urlpatterns = [
     path('courses/', ListCourseView.as_view(), name="course-list"),  
     path('courses/<int:pk>', DetailCourseView.as_view(), name="course-detail"),
     path('collections/', ListCollectionView.as_view(), name="collection-list"),
     path('collections/<int:pk>', DetailCollectionView.as_view(), name="collection-detail"),
     path('quizs/', ListQuizView.as_view(), name="quiz-list"),
     path('quizs/<int:pk>', DetailQuizView.as_view(), name="quiz-detail"),
     path('questions/', ListQuestionView.as_view(), name="question-list"),
     path('questions/<int:pk>', DetailQuestionView.as_view(), name="question-detail"),
     path('quiztakers/', ListQuizTakerView.as_view(), name="quiztaker-list"),
     path('quiztakers/<int:pk>', DetailQuizTakerView.as_view(), name="quiztaker-detail"),
       path('answers/', ListAnswerView.as_view(), name="answer-list"),
     path('answers/<int:pk>', DetailAnswerView.as_view(), name="answer-detail"),
]