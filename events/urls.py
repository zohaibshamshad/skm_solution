from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('', views.EventsListView.as_view(), name='events'),
    path('<slug:pk>', views.EventDetailView.as_view(), name='event'),
    path('tasks/', views.tasks, name='tasks'),
]
