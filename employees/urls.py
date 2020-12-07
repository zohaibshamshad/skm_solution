from django.contrib import admin
from django.urls import path, include
from employees import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees', views.EmployeeView)

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='employees'),
    path('index/', views.index, name='index'),
    path('<slug:pk>', views.EmployeesDetailView.as_view(), name='employee'),
    path('api/', include(router.urls)),
]
