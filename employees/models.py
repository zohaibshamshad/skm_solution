from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Employee(models.Model):
    e_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=60)
    designation = models.CharField(max_length=100)
    dob = models.DateTimeField(default=datetime.now)
    cnic = models.CharField(max_length=13)
    email = models.CharField(max_length=60, blank=True)
    hire_date = models.DateTimeField(default=datetime.now)
    qualification = models.CharField(max_length=100)
    scale = models.CharField(max_length=60)
    gross_salary = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(30000000)])
    experience = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(80)])
    jd = models.TextField(blank=True)
    department = models.CharField(max_length=60, default='Safety & Security Department')
    phone_main = models.CharField(max_length=11)
    phone_1 = models.CharField(max_length=11, blank=True)
    phone_2 = models.CharField(max_length=11, blank=True)
    home_phone = models.CharField(max_length=11, blank=True)
    spouse_phone = models.CharField(max_length=11, blank=True)
    children = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(30)])
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_available = models.BooleanField(default=True)
    rating = models.IntegerField(default=0, validators = [MinValueValidator(0), MaxValueValidator(5000)])
    listing_date = models.DateTimeField(default=datetime.now)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.e_code