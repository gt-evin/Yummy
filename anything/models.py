from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=100)
    date = models.DateField(null=True)

    def __str__(self):
        return self.username

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_number = models.IntegerField()


    def __str__(self):
        return self.product_name


class Member(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=100)
    people = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
