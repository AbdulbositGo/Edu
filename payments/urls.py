from django.urls import path

from . import views

urlpatterns = [
    path('registries/', views.registry_list_create, ),
    path('registries/<int:pk>/', views.registry_retrive_update_delete, ),

    path('payments/', views.payment_list_create, ),
    path('payments/<int:pk>/', views.payment_retrive_update_delete, ),
]