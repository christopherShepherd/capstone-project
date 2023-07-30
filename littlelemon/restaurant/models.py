from django.db import models
from django.core.validators import MaxValueValidator


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(999999)])
    booking_date = models.DateTimeField()


class Menu(models.Model):
    id = models.AutoField(primary_key=True, validators=[MaxValueValidator(99999)])
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0, validators=[MaxValueValidator(99999)])

    def __str__(self): 
        return self.title
