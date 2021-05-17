from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime

# I'm creating my first models here!.
class School(models.Model):     
        
        name = models.CharField(max_length = 50)
        address = models.CharField(max_length= 50)
        postal_code = models.IntegerField()

        
   
class Faculty(models.Model):
    
        name = models.CharField(max_length = 50)
        
        

class Department(models.Model):
    
        name = models.CharField(max_length = 50)
        faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

        


class Certificate_Type(models.Model):
    
        name = models.CharField(max_length = 50)

        


class Grade(models.Model):
            
        grade_type = models.FloatField(max_length= 5)
        

class Student(models.Model):
    
        
        full_name = models.CharField(max_length = 50)
        year_of_graduation = models.DateField(auto_now=datetime.year)
        department = models.ForeignKey(Department, on_delete=models.CASCADE)
        grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
        school = models.ForeignKey(School, on_delete=models.CASCADE)
        certifcate_type = models.ForeignKey(Certificate_Type, on_delete=models.CASCADE)
        
        


