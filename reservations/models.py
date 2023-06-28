from django.db import models
from django.contrib.auth.models import User

class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    kundennummer = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    login = models.URLField()
    url = models.URLField()

    def __str__(self):
        return self.name
    

class Apartment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_contract = models.DateField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_day = models.DateField()
    num_guests = models.IntegerField()
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    purpose = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    t_sum = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    rech_num = models.CharField(max_length=255)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    link_reservation = models.URLField()
    guest_document = models.FileField(upload_to='guest_documents/') 
    link = models.URLField()

    def __str__(self):
        return f"Reservation {self.id}"



