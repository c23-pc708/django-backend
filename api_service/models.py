from django.db import models
import json

# Create your models here.


class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    # https://stackoverflow.com/questions/22340258/list-field-in-model
    type = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    opening_time = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
