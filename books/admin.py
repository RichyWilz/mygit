from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.site_header = 'LIBRARY ADMINISTRATION'
admin.site.register(Book)