from django.db import models


class Sportsman(models.Model):
    name = models.CharField(max_length=128)
    sport = models.CharField(max_length=128)
    photo = models.URLField()
    country = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sportsman"
        verbose_name_plural = "Sportsmen"
