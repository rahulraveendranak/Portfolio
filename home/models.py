from django.db import models

# Create your models here.
class Contact(models.Model):
   name = models.TextField(max_length = 50)
   email = models.CharField(max_length=50)
   phone = models.CharField(max_length=10)
   desc = models.TextField()