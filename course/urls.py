from django.urls import path
from .views import CourseListAPIView, CourseCreateAPIView, CourseDeleteAPIView, CourseUpdateAPIView, CourseDetailAPIView


urlpatterns = [
    path('list/', CourseListAPIView.as_view(),name='course_list'),
    path('create/', CourseDetailAPIView.as_view(),name='course_create'),
    path('detail/<int:pk>/', CourseCreateAPIView.as_view(),name='course_detail'),
    path('update/<int:pk>/', CourseUpdateAPIView.as_view(),name='course_update'),
    path('delete/<int:pk>/', CourseDeleteAPIView.as_view(),name='course_delete'),

]