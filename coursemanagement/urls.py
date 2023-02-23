from django.urls import path
from .views import ListCourseView, DetailCourseView, ListCollectionView, DetailCollectionView

urlpatterns = [
     path('courses/', ListCourseView.as_view(), name="course-list"),  
     path('courses/<int:pk>', DetailCourseView.as_view(), name="course-detail"),
     path('collections/', ListCollectionView.as_view(), name="collection-list"),
     path('collections/<int:pk>', DetailCollectionView.as_view(), name="collection-detail"),
]