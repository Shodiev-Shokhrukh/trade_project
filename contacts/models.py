from datetime import datetime

from django.db import models


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=60)
    message = models.TextField(blank=True, max_length=5000)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
