from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='employees'),
    path('index', views.index, name='index'),
    path('<slug:pk>', views.EmployeesDetailView.as_view(), name='employee'),
]
