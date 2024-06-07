from django.db import models

# Create your models here.

class Landlord(models.Model):
    land_id=models.CharField(max_length=15, primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=16)
    contact=models.CharField(max_length=50)

    

