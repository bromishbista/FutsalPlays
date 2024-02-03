from django.db import models
from django.contrib.auth.models import User


# model for contact for form in user acc
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    message = models.TextField(max_length=350)

    def _str_(self):
        return str(self.full_name)

    