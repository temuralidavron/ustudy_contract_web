from rest_framework import serializers
from .models import CourseInfo

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            "id",
            "title",
            'description',
            'price',
            'duration',
            'salary_middle'

        ]



class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            "title",
            'description',
            'price',
            'duration',
            'salary_middle'

        ]

class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            "title",
            'description',
            'price',
            'duration',
            'salary_middle'

        ]


class CourseDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            "title",
            'description',
            'price',
            'duration',
            'salary_middle'
        ]


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            "id",
            "title",
            'description',
            'price',
            'duration',
            'salary_middle'
        ]