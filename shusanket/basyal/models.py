from pyexpat import model
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    address= models.CharField(max_length=100)