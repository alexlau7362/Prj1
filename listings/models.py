# Listing -> Models
from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here. 
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)  # Increased max_digits
    clubhouse = models.IntegerField(default=0)
    sqft = models.IntegerField()
    estate_size = models.FloatField(default=0.0)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')  # Fixed `upload_to`
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Fixed `upload_to`
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Fixed `upload_to`
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Fixed `upload_to`
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Fixed `upload_to`
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Fixed `upload_to`
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Fixed `upload_to`
         
    def __str__(self):
        return f"House Title: {self.title}"