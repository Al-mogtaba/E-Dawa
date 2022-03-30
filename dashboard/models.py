from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Locations(models.Model):
    locations = models.CharField(max_length=300, null=True)
    def __str__(self):
            return str(self.locations)

class Pharmacy(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    pharmacy_name = models.CharField(max_length=200, null=True,)
    location = models.ForeignKey(Locations, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=300, null=True,)
    google_map_link = models.CharField(max_length=300, null=True,)

    def __str__(self):
        return str(self.pharmacy_name)
    def get_absolute_url(self):
        return reverse("dashboard")
    
    
class Medicine(models.Model):
    owner = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=200)
    comapny = models.CharField(max_length=200)
    def __str__(self):
        return str(self.medicine_name)
    
    def get_absolute_url(self):
        return reverse("item_list")
    