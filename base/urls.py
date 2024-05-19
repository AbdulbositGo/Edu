from django.urls import path

from . import views

urlpatterns = [
    path('teachers/', views.teacher_list_create, ),
    path('teachers/<int:pk>/', views.teacher_retrive_update_delete, ),

    path('students/', views.student_list_create, ),
    path('students/<int:pk>/', views.student_retrive_update_delete, ),
    
]
