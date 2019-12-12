import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Destination(models.Model):
    dest_image_path = models.CharField(max_length=500, default = "", blank = True)
    dest_name = models.CharField(max_length=255, default = "", blank = True)
    dest_country = models.CharField(max_length=30, default=""),
    dest_desc = models.TextField(max_length=2000, default = "", blank = True)
    dest_short_desc = models.TextField(max_length=100, default = "", blank = True)
    dest_checkin = models.DateField('Check in', auto_now_add = True)
    dest_checkout = models.DateField('Check out', auto_now_add = True)
    dest_price = models.IntegerField(default=0)
    dest_rating = models.FloatField(default=0)

    def __str__(self):
        return self.dest_name

class User(models.Model):
    picture = models.CharField(max_length=500, default="")
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    join_date = models.DateTimeField("Joined")
    update_date = models.DateTimeField(auto_now=True)