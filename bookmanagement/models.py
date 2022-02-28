from django.db import models


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
