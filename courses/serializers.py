from rest_framework import serializers

from .models import Category, Subject, Course


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]
    

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            "id",
            "category",
            "name",
        ]
        


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "subject",
            "teacher",
            "starting_date",
            "price",
        ]
        