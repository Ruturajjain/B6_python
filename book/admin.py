from django.contrib import admin
from .models import Book
# Register your models here.
print("in admin.py")
admin.site.register(Book)