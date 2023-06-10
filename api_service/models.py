from django.db import models
import json


# Create your models here.
class Destination(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    art = models.IntegerField(blank=True, null=True)
    entertainment = models.IntegerField(blank=True, null=True)
    sightings = models.IntegerField(blank=True, null=True)
    culinary = models.IntegerField(blank=True, null=True)
    shopping = models.IntegerField(blank=True, null=True)
    image_link = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    weekdays_time = models.TextField(blank=True, null=True)
    weekend_time = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=8, decimal_places=7, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, blank=True, null=True
    )
    lowest_price = models.IntegerField(blank=True, null=True)
    highest_price = models.IntegerField(blank=True, null=True)
    additional_price = models.IntegerField(blank=True, null=True)
    column_1_star = models.IntegerField(blank=True, null=True)
    column_2_star = models.IntegerField(blank=True, null=True)
    column_3_star = models.IntegerField(blank=True, null=True)
    column_4_star = models.IntegerField(blank=True, null=True)
    column_5_star = models.IntegerField(blank=True, null=True)
    total_reviews = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    location_link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "destination"
