from django.db import models
from datetime import datetime

# I'm creating my first models here!.
class Student(models.Model):
    full_name = models.CharField(max_length = 50)
    year_of_graduation = models.IntegerField()
    department = models.CharField(max_length= 50)
    grade = models.IntegerField()
    school = models.CharField(max_length = 50)
    certifcate_type = models.CharField(max_length = 50)
    

class School(models.Model):
    name = models.CharField(max_length = 50)

class Faculty(models.Model):
    name = models.CharField(max_length = 50)

class Department(models.Model):
    name = models.CharField(max_length = 50)
    Faculty

class Certificate_Type(models.Model):
    name = models.CharField(max_length = 50)

class Grade(models.Model):
    type = models.IntegerField()