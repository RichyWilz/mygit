from datetime import datetime
from django.db import models
 #import datetime

# Create your models here.
class Book(models.Model):
    title            = models.CharField(max_length=40)
    publication_date = models.DateField()
    subject_area     = models.CharField(max_length=15)
    author           = models.CharField(max_length=40)
    description      = models.TextField()
    cover_photo      = models.FilePathField(path="books\images")

    def __str__(self) :
        return self.title
