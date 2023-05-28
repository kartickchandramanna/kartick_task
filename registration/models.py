from django.db import models


class Address(models.Model):
    street_name = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

class Car(models.Model):
    model_name = models.CharField(max_length=20)
    manufacturing_date = models.DateTimeField()
    manufacturer = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
