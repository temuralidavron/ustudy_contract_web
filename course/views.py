from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from course.models import CourseInfo
from course.serializers import CourseDetailSerializer, CourseListSerializer, CourseCreateSerializer, \
    CourseUpdateSerializer, CourseDeleteSerializer


# Create your views here.


class CourseListAPIView(generics.ListAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsAuthenticated]


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [IsAuthenticated]


class CourseUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseUpdateSerializer
    permission_classes = [IsAuthenticated]



class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseDeleteSerializer
    permission_classes = [IsAuthenticated]