from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Employee(models.Model):
    e_code = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_main = models.CharField(max_length=200)
    phone_1 = models.CharField(max_length=200, blank=True)
    phone_2 = models.CharField(max_length=200, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_available = models.BooleanField(default=True)
    salary = models.IntegerField()
    rating = models.IntegerField(
        default=0,
        validators = [MinValueValidator(0), MaxValueValidator(5000)]
        )
    join_date = models.DateTimeField(default=datetime.now)
    listing_date = models.DateTimeField(default=datetime.now)
    jd = models.TextField(blank=True)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200, default='Safety & Security Department')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.e_code