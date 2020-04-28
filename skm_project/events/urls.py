from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('', views.events, name='events'),
    path('<int:event_id>', views.event, name='event'),
    path('tasks/', views.tasks, name='tasks'),
]
