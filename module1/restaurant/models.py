from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=253)
    no_of_guests = models.SmallIntegerField()
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()