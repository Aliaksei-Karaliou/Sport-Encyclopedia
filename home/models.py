from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField


class Club(models.Model):
    name = models.CharField(max_length=128)
    logo = models.URLField()
    country = CountryField()
    year = models.IntegerField(validators=[MinValueValidator(1850), MaxValueValidator(2100)], blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128, blank=True)
    photo = models.URLField(blank=True)
    country = CountryField()
    club = models.OneToOneField(Club, blank=True)

    def __str__(self):
        return self.display_name if self.display_name else self.first_name + " " + self.last_name


class Coach(Person):
    class Meta:
        verbose_name_plural = "Coaches"


class Player(Person):
    position = models.CharField(max_length=128)
