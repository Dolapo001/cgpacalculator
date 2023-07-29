from django.db import models


class Student(models.Model):
    matric_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)


class Semester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester_number = models.PositiveIntegerField()
    grades = models.CharField(max_length=100, default='')
    course_units = models.CharField(max_length=100, default='')
