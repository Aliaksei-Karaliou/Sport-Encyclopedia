from django.db import models
from django_countries.fields import CountryField


class League(models.Model):
    name = models.CharField(max_length=64)
    country = CountryField(max_length=64)
    level = models.IntegerField(blank=True, null=True, default=1)
    info = models.TextField(blank=True, null=True, default=None)
    logo = models.ImageField(blank=True, null=True, default=None, upload_to='league')

    def __str__(self):
        return "%s (%s, D%s)" % (self.name, self.country.name, self.level)


class Club(models.Model):
    name = models.CharField(max_length=64)
    country = CountryField()
    city = models.CharField(max_length=64)
    stadium = models.CharField(max_length=64)
    league = models.ForeignKey(League, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, default=None, upload_to='club')

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    club = models.ForeignKey(Club, blank=True, null=True)
    country = CountryField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='person')

    def __str__(self):
        return self.display_name if self.display_name else "%s %s" % (self.first_name, self.last_name)


class Player(Person):
    shirt_number = models.IntegerField(blank=True, null=True, default=None)



class Coach(Person):
    pass
