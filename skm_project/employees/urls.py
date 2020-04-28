from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('', views.employees, name='employees'),
    path('index', views.index, name='index'),
    path('<int:employee_id>', views.employee, name='employee'),
]
