from django.db import models
from django.contrib.auth.models import User
from geopy.geocoders import Nominatim

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    cuisine = models.CharField(max_length=100, blank=True, null=True)
    price_range = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
    x_coordinate = models.IntegerField(default=0)
    y_coordinate = models.IntegerField(default=0)
    width = models.IntegerField(default=50)
    height = models.IntegerField(default=50)

    def __str__(self):
        return f"Table {self.table_number} in {self.restaurant.name}"

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="restaurant_booking")  # Замените "restaurant_booking" на что-то уникальное
        location = geolocator.geocode(self.address)
        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude
        super().save(*args, **kwargs)