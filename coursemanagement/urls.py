from django.urls import path
from .views import ListCourseView, DetailCourseView, ListCollectionView

urlpatterns = [
     path('courses/', ListCourseView.as_view(), name="course-list"),  
     path('courses/<int:pk>', DetailCourseView.as_view(), name="course-detail"),
     path('collections/', ListCollectionView.as_view(), name="collection-list"),
]