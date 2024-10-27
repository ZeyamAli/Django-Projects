from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

