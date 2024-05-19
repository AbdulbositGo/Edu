from django.urls import path


from . import views

urlpatterns = [
    path('categories/', views.category_list_create, ),
    path('categories/<int:pk>/', views.category_retrive_update_delete, ),

    path('subjects/', views.subject_list_create, ),
    path('subjects/<int:pk>/', views.subject_retrive_update_delete, ),
    
    path('courses/', views.course_list_create, ),
    path('courses/<int:pk>/', views.course_retrive_update_delete, ),
]