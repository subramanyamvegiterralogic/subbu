from django.db import models

# Create your models here.

class Employee(models.Model):
    e_no = models.CharField(max_length = 10)
    e_name = models.CharField(max_length = 64)
    e_sal = models.FloatField()
    e_mobile = models.CharField(max_length = 13)
    e_city = models.CharField(max_length = 64, default='San Jose')

class Education(models.Model):
    e_no = models.CharField(max_length = 10)
    highest_qualification = models.CharField(max_length = 64)
    temporary_address = models.CharField(max_length = 128)
    permanent_address = models.CharField(max_length = 128)
    
