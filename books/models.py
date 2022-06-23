from django.db import models
 #import datetime

# Create your models here.
class Book(models.Model):
    title            = models.CharField(max_length=120)
    publication_date = models.DateField()
    subject_area     = models.CharField(max_length=40)
    author           = models.CharField(max_length=80)
     #availability     = models.ForeignKey
    description      = models.TextField()
    cover_photo      = models.FilePathField(path="/images")

