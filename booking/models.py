from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

#group chat models


# Create your models here.
class Futsal(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    location = models.CharField(max_length=200)
    location_url = models.CharField(max_length=700, null=True)
    owner = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    description = models.TextField(max_length=800)
    price = models.IntegerField(default=10)
    
    def __str__(self):
        return self.name


class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    team_image = models.ImageField(upload_to='img/', null=True, blank=False)
    location_url= models.CharField(max_length=200, null=False, default='location')
    location = models.CharField(max_length=200)
    join_date = models.DateTimeField(auto_now_add=False)
    players = models.IntegerField()

    def __str__(self):
        return self.name


