from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forms/', views.form_list, name='form_list'),
    path('forms/create/', views.form_create, name='form_create'),
    path('forms/<int:pk>/', views.form_render, name='form_render'),
    path('forms/<int:form_id>/add_field/', views.form_field_add, name='form_field_add'),
    
]
