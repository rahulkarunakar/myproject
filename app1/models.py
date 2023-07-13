from django.db import models

class customer(models.Model):
    uname = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

class booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=100)
    message = models.CharField(max_length=150)
    variant = models.CharField(max_length=100,default=10)
    price = models.CharField(max_length=100,default=10)