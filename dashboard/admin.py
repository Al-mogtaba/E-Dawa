from django.contrib import admin
from .models import Pharmacy, Medicine, Locations

# Register your models here.
admin.site.register(Pharmacy)
admin.site.register(Medicine)
admin.site.register(Locations)
