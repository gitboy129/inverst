from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=30)
    password=models.IntegerField()