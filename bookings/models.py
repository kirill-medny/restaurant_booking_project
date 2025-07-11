from django.contrib.auth.models import User
from django.db import models

from restaurants.models import Table


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.number_of_guests} on {self.date} at {self.time} at {self.table}"
