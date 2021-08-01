from django.db import models
from django.db.models.fields import (
    BooleanField, CharField, TextField, URLField)
from django.db.models.fields.files import ImageField


# Create your models here.
class SocialLink(models.Model):

    name = CharField(max_length=25)
    hyperlink = URLField(blank=True)
    icon = CharField(max_length=50)
    display = BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)


class Skill(models.Model):

    name = CharField(max_length=25)
    description = TextField(blank=True)
    icon = CharField(max_length=50)
    display = BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)


class Testimonial(models.Model):

    name = CharField(max_length=25)
    info = CharField(max_length=25)
    description = TextField(blank=True)
    image = ImageField(upload_to='customers')

    def __str__(self):
        return '{}'.format(self.name)


class Bio(models.Model):

    name = CharField(max_length=25)
    description = TextField(blank=True)
    short_description = CharField(max_length=256, blank=True)
    practice = TextField(blank=True)
    image = ImageField(upload_to='profile', blank=True)
    image_circle = ImageField(upload_to='profile', blank=True)

    def __str__(self):
        return '{}'.format(self.name)
