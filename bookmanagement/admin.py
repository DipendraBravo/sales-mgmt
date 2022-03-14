from django.contrib import admin
from .models import Book, UserRequest

# Register your models here.
admin.site.register(Book)
admin.site.register(UserRequest)