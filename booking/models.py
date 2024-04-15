from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

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


class Match(models.Model):
    futsal = models.ForeignKey(Futsal, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_team')
    first_image = models.ImageField(upload_to='img/', null=True, blank=False)
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='second_team')
    second_image = models.ImageField(upload_to='img/', null=True, blank=False)
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)
    player = (
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('14','14'),
        ('16','16'),
        ('20','20'),
    )
    playercount = models.CharField(max_length=150,choices=player, default='5')
    game = (
        ('friendly match','friendly match'),
        ('losers match','losers match'), 
    )
    gametype = models.CharField(max_length=150,choices=game, default='friendly match')




from datetime import datetime, timedelta

class Book_futsal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    futsal = models.ForeignKey(Futsal, on_delete=models.CASCADE)
    date = models.DateField(null=True)   
    start_time = models.TimeField(choices=[(datetime.strptime(f'{i}:00', '%H:%M').time(), f'{i}:00 {datetime.strptime(f"{i}:00", "%H:%M").strftime("%p")}') for i in range(10, 18)])
    duration = models.PositiveIntegerField(choices=[(i, f"{i} hour{'s' if i>1 else ''}") for i in range(1, 6)], default=1)

    def end_time(self):
        return (datetime.combine(datetime.today(), self.start_time) + timedelta(hours=self.duration)).time()
   




class Testimonials(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=600)
    image = models.ImageField(upload_to='img/', null=True, default='img/testimonial.jpg')


class Blog(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    small_description = models.CharField(max_length=250, null=False, blank=False)
    description = RichTextField(null=True, blank=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    image =  models.ImageField(upload_to='img/', null=True, blank=False)
    description = RichTextField(null=True, blank=True)

    def _str_(self):
        return str(self.title)

#need to rename later
class Beadcrumbs(models.Model):
    Total_Join_Teams = models.IntegerField()
    Total_Play_Games = models.IntegerField()
    Total_Players = models.IntegerField()
    Total_Futsal_Ground = models.IntegerField()
    Total_Winner_Teams = models.IntegerField()


class Gallery(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    image =  models.ImageField(upload_to='img/', null=True, blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.title)



class slider(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=800, null=False, blank=False)
    image = models.ImageField(upload_to='img/', null=True, blank=False)

    def __str__(self):
        return self.title


class Details(models.Model):
    name = models.CharField(max_length=200)
    location_url= models.CharField(max_length=200, null=False, default='location')
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='img/', null=True, blank=False)
    email = models.EmailField(max_length=800)
    website = models.CharField(max_length=100)
    footer_description = models.TextField(max_length=500, null=False, default='location')
    
    def __str__(self):
        return self.name
    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    futsal = models.ForeignKey(Futsal, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.futsal.name}'
    

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    futsal = models.ForeignKey(Futsal, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)




from .models import Futsal, Book_futsal, Review, User
