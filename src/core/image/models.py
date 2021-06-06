from django.db import models
from django.contrib.postgres.fields import ArrayField

class Item(models.Model):
    name = models.CharField(max_length=50)
    phone = models.DecimalField(max_digits=10,decimal_places=0)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    encodings = ArrayField(ArrayField(models.DecimalField(decimal_places=10,max_digits=100)),blank=True,default=list)

class Document(models.Model):
    docfile = models.FileField(upload_to='images/')