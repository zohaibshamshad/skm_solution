# Generated by Django 3.0.5 on 2020-04-25 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='point',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)]),
        ),
    ]