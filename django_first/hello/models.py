from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=16)
    user_age = models.IntegerField(default=1)