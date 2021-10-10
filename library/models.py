from django.db import models
from datetime import date, timedelta
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    rollNo = models.IntegerField()
    departmentName = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.studentName
    


class Book(models.Model):
    bookName = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    isbnNumber = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bookName

class IssueBook(models.Model):
    StudentName = models.CharField(max_length=50, default=None)
    StudentID = models.IntegerField()
    BookName = models.CharField(max_length=50,default=None)
    ISBN_Number = models.CharField(max_length=50,default=None)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=date.today() + timedelta(days=7))
    
    
