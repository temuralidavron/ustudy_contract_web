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
            'initial_price',
            'monthly_duration',

        ]



class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            "title",
            'description',
            'price',
            'monthly_duration',
            'salary_middle',


        ]

class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            'id',
            "title",
            'description',
            'price',
            'monthly_duration',
            'salary_middle'

        ]


class CourseDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseInfo
        fields =[
            'id',
            "title",
            'description',
            'price',
            'monthly_duration',
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
            'monthly_duration',
            'salary_middle'
        ]