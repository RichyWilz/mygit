#from datetime import datetime
from ast import Pass
from django.db import models
from datetime import date

# Create your models here.
class Student(models.Model):
    username   = models.CharField(max_length= 15)
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30) #help_text= 'Optional')
    email      = models.EmailField(max_length=200) #help_text = 'Enter valid e-mail address')
    course     = models.CharField(max_length= 35)

    def __str__(self) :
        return self.username

class Book(models.Model):
    title            = models.CharField(max_length=40)
    publication_date = models.DateField()
    subject_area     = models.CharField(max_length=15)
    author           = models.CharField(max_length=40)
    description      = models.TextField()
    cover_photo      = models.ImageField(null=True, blank=True, upload_to='images/')
    status           = models.CharField(max_length=10,default='Available')

    def __str__(self) :
        return self.title

 # )
class Borrow(models.Model):
    #student_name  = models.ForeignKey('Student', on_delete=models.CASCADE)
    book_title    = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrow_date   = models.DateField()
    return_date   = models.DateField()
    email_address = models.EmailField('Email Field',default='somoneone@gmail.com')
    fine          = models.BooleanField(default=False)

    def __str__(self):
        return self.book_title
    # use this in table that will leep track of days
    @property
    def Days_remaining(self):
        today = date.today()
        days_remaining= self.return_date.date() - today
        return days_remaining

    @property
    def Days_past(self):
        today = date.today()
        if self.return_date < today:
            returned = "PAST"
        else:
            Pass
        return returned

