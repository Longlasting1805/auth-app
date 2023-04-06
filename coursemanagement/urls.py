from django.urls import path
from .views import CourseView, CollectionView


urlpatterns = [
     path('courses/', CourseView.as_view(), name="create-course"),  
     path('collections/', CollectionView.as_view(), name="collection"),
     # path('quizs/', ListQuizView.as_view(), name="quiz-list"),
     # path('quizs/<int:pk>', DetailQuizView.as_view(), name="quiz-detail"),
     # path('questions/', ListQuestionView.as_view(), name="question-list"),
     # path('questions/<int:pk>', DetailQuestionView.as_view(), name="question-detail"),
     # path('quiztakers/', ListQuizTakerView.as_view(), name="quiztaker-list"),
     # path('quiztakers/<int:pk>', DetailQuizTakerView.as_view(), name="quiztaker-detail"),
     # path('answers/', ListAnswerView.as_view(), name="answer-list"),
     # path('answers/<int:pk>', DetailAnswerView.as_view(), name="answer-detail"),
     # path('assignments/', ListAssignmentView.as_view(), name="assignment-list"),
     # path('assignments/<int:pk>', DetailAssignmentView.as_view(), name="assignment-detail"),
     # path('submissions/', ListSubmissionView.as_view(), name="submission-list"),
     # path('submissions/<int:pk>', DetailSubmissionView.as_view(), name="submission-detail"),
]