from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)

class Students(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)    
