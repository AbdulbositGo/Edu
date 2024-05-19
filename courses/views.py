from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Category, Subject, Course
from .serializers import CategorySerializers, SubjectSerializers, CourseSerializers

class CategoryListCreateApiView(ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    lookup_field = 'pk'


class SubjectListCreateApiView(ListCreateAPIView):
    serializer_class = SubjectSerializers
    queryset = Subject.objects.all()


class SubjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializers
    queryset = Subject.objects.all()
    lookup_field = 'pk'


class CourseListCreateApiView(ListCreateAPIView):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    lookup_field = 'pk'


category_list_create = CategoryListCreateApiView.as_view()
course_list_create = CourseListCreateApiView.as_view()
subject_list_create = SubjectListCreateApiView.as_view()

category_retrive_update_delete = CategoryRetrieveUpdateDestroyAPIView.as_view()
subject_retrive_update_delete = SubjectRetrieveUpdateDestroyAPIView.as_view()
course_retrive_update_delete = CourseRetrieveUpdateDestroyAPIView.as_view()