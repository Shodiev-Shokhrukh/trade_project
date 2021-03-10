from datetime import datetime

from django.db import models


# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/realtors/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
