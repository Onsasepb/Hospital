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
        return self.fullname


class Products(models.Model):
    name = models.CharField(max_length=15)
    product_price = models.CharField(max_length=10)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Patient(models.Model):
    fullname = models.CharField(max_length=100, default="precious")
    email = models.EmailField()
    phone = models.CharField(max_length=12, default=725371846)
    date = models.DateField(default=12 / 12 / 2024)
    department = models.CharField(max_length=100, default="department 1")
    doctor = models.CharField(max_length=70, default="surgeon")
    message = models.TextField(default="i have been on previous medicine")

    def __str__(self):
        return self.fullname
