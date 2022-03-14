from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    edition = models.CharField(max_length=50)
    unitprice = models.IntegerField()
    in_stock = models.IntegerField()
    image = models.ImageField(upload_to='cover/')
    totalprice = models.IntegerField(blank=True)

    def __str__(self):
        return self.book_name


class UserRequest(models.Model):
    status_choices = [
        ('cancel', 'cancel'),
        ('delivered', 'delivered'),
        ('requested', 'requested'),
    ]

    username = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=20)
    book_quantity = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    delivered_status = models.CharField(
        max_length=50,
        choices=status_choices,
        default='requested',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


# @receiver(pre_save, sender=UserRequest)
# def update_book(sender, instance, **extra_fields):
#     if instance.created_at == instance.updated_at:
#         breakpoint()
