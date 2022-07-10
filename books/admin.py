from django.contrib import admin
from .models import Book,Student,Borrow
# Register your models here.
admin.site.site_header = 'LIBRARY ADMINISTRATION'
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrow)