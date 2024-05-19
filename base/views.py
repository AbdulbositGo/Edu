from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Teacher, Student
from .serializers import TeacherSerializers, StudentSerializers

class TeacherListCreateApiView(ListCreateAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()


class TeacherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()
    lookup_field = 'pk'


class StudentListCreateApiView(ListCreateAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()
    lookup_field = 'pk'



teacher_list_create = TeacherListCreateApiView.as_view()
student_list_create = StudentListCreateApiView.as_view()

teacher_retrive_update_delete = TeacherRetrieveUpdateDestroyAPIView.as_view()
student_retrive_update_delete = StudentRetrieveUpdateDestroyAPIView.as_view()