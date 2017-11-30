from django.db import models


class Sportsman(models.Model):
    name = models.CharField(max_length=128)
    sport = models.CharField(max_length=128)
    photo = models.URLField()
    country = models.CharField(max_length=128)
