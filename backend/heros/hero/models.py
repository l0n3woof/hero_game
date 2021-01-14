from django.db import models

# Create your models here.

class stats(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default='Alive')
