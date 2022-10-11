from django.db import models
from django.db.models.fields import DateField, EmailField
from versatileimagefield.fields import VersatileImageField


class Update(models.Model):
    title = models.CharField(max_length=100)
    image = VersatileImageField(upload_to='update')
    details = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = VersatileImageField(upload_to='gallery')

    def __str__(self):
        return str(self.title)


class Position(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Award(models.Model):
    title = models.CharField(max_length=100)
    image = VersatileImageField(upload_to='award')
    subject = models.CharField(max_length=100)
    date = DateField(blank=True, null=True)
    place = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


TIME_CHOICES = (
    ('09300950', '9:30 am - 9:50 am'),
    ('10001020', '10:00 am - 10:20 am'),
    ('10301050', '10:30 am - 10:50 am'),
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=100)
    time = models.CharField(max_length=128,choices=TIME_CHOICES)
    email = EmailField(max_length=100)
    date = models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.name)
