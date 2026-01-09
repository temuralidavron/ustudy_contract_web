from django.shortcuts import render
from rest_framework import generics

from course.models import CourseInfo
from course.serializers import CourseDetailSerializer, CourseListSerializer, CourseCreateSerializer, \
    CourseUpdateSerializer, CourseDeleteSerializer


# Create your views here.


class CourseListAPIView(generics.ListAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseListSerializer


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseDetailSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseCreateSerializer


class CourseUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseUpdateSerializer



class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseDeleteSerializer