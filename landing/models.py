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
    city = models.CharField(max_length=64, blank=True, null=True, default=None)
    stadium = models.CharField(max_length=64, blank=True, null=True, default=None)
    league = models.ForeignKey(League, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, default=None, upload_to='club')
    info = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    club = models.ForeignKey(Club, blank=True, null=True)
    country = CountryField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='person')
    bdate = models.DateField(blank=True, null=True, default=None)
    info = models.TextField(blank=True, null=True, default=None)

    @property
    def full_name(self):
        return self.display_name if self.display_name else "%s %s" % (self.first_name, self.last_name)

    @property
    def age(self):
        today = self.bdate.today()
        return today.year - self.bdate.year - ((today.month, today.day) < (self.bdate.month, self.bdate.day))

    def __str__(self):
        return self.display_name if self.display_name else "%s %s" % (self.first_name, self.last_name)


class Player(Person):
    shirt_number = models.IntegerField(blank=True, null=True, default=None)
    is_captain = models.BooleanField(blank=True, default=False)


class Coach(Person):
    pass


class PlayerHistory(models.Model):
    player = models.ForeignKey(Player)
    club = models.ForeignKey(Club, blank=True, null=True, default=None)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, default=None)
    matches = models.IntegerField(blank=True, default=None)
    goals = models.IntegerField(blank=True, default=None)
    is_loan = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = "Player history"
        verbose_name_plural = "Player histories"

    def __str__(self):
        return "%s - %s (%s-%s) %s" % (
            self.player, self.club.name, self.start_year, self.end_year if self.end_year else '...',
            "loan" if self.is_loan else "")
