from django.db import models
from django.contrib.auth.models import User

class UserGroups(models.Model):
    group_name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, related_name='user_groups')

    def __str__(self):
        return self.group_name
    
# message for form message 
from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)


