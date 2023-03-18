from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class courses(models.Model):
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.course



class students(models.Model):
    student_Key = models.CharField(max_length=10,default='STUD')
    student_username = models.ForeignKey(User, on_delete=models.CASCADE) #AZATSCS013
    student_name = models.CharField(max_length=30)
    student_dob = models.CharField(max_length=30)#PASSWORD
    student_admissionyear = models.CharField(max_length=30)
    student_course = models.ForeignKey(courses, on_delete=models.CASCADE)
    def __str__(self):
        return self.student_username

# class staffs(models.Model):
#     staff_Key = models.CharField(max_length=30,default='FAC')
#     staff_username = models.ForeignKey(User, on_delete=models.CASCADE)
#     staff_name = models.CharField(max_length=30)
#     staff_gender = models.CharField(max_length=30)
#     staff_dob = models.CharField(max_length=30)
#     staff_address = models.CharField(max_length=200)
#     staff_phone =models.CharField(max_length=30)
#     staff_yearofjoin = models.CharField(max_length=30)
#     def __str__(self):
#         return self.staff_name