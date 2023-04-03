from django.db import models


class Topic(models.Model):
    """Daily topic"""
    date = models.DateField()
    topic = models.CharField(max_length=255)
    body = models.TextField(default='')
    picture = models.ImageField(upload_to='images/', blank=True, default='images/images/auto.jpg')
