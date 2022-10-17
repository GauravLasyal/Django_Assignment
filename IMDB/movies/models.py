from django.db import models

# Create your models here.


class MovieTable(models.Model):
	rank=models.IntegerField()
	name=models.CharField(max_length=255)
	rating=models.FloatField()
	desc=models.CharField(max_length=1000)
	
