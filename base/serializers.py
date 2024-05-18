from rest_framework import serializers

from .models import Teacher, Student


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "birth_date",
            "address",
            "salary",
        ]
    

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "birth_date",
            "address",
        ]
        