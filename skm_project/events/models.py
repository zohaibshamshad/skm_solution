from django.db import models
from employees.models import Employee
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from datetime import datetime


class Event(models.Model):
    name = models.CharField(max_length=28)
    location = models.CharField(max_length=28)
    event_date = models.DateTimeField()
    description = models.TextField(blank=True)
    is_repeated = models.BooleanField()
    managed_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    is_completed = models.BooleanField(default=False)
    total_point = models.IntegerField(
        validators = [MinValueValidator(5), MaxValueValidator(100)]
        )
    point_recieved = models.IntegerField(
        default=0,
        validators = [MaxValueValidator(100),]
        )
    percentage = models.IntegerField(default=0)
    deadline = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True)
    task_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.name