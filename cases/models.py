from django.db import models
from datetime import date

# Create your models here.

CLASSIFICATION_CHOICES = [
    ('MISSING PERSON', 'Missing Person'),
    ('MYSTERIOUS DEATH', 'Mysterious Death'),
    ('UNSOLVED HOMICIDE', 'Unsolved Homicide'),
    ('COURT', 'In Legal System'),
    ('CLOSED', 'Resolved in court system')]


def name_folder_path(instance, filename):
    return 'image_{0}{1}/{2}'.format(instance.first_name, instance.last_name, filename)


class Vanished(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    missing_since = models.DateField(blank=True, null=True, help_text="Format: yyyy-mm-dd")
    missing_from = models.CharField(max_length=150, blank=True)
    classification = models.CharField(max_length=40, choices=CLASSIFICATION_CHOICES, default='MISSING')
    sex = models.CharField(max_length=2, blank=True)
    race = models.CharField(max_length=10, blank=True)
    dob = models.DateField("Date of Birth", blank=True, null=True, help_text="Format: yyyy-mm-dd")
    age = models.IntegerField(blank=True, help_text="Age when went missing")
    description = models.TextField(blank=True)
    narrative = models.TextField(blank=True)
    enrolled = models.BooleanField(blank=True)
    tribe = models.TextField(blank=True)
    photo = models.ImageField(upload_to=name_folder_path, blank=True)
    agency = models.TextField(blank=True)
    sources = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + self.last_name


class Story(models.Model):
    url = models.URLField(blank=True)
    hed = models.TextField(blank=True)
    pub_date = models.DateField(null=True)
    vanished = models.ManyToManyField(Vanished, related_name="stories")

    def __str__(self):
        return self.hed


class Point(models.Model):
    lat = models.FloatField("latitude")
    lon = models.FloatField("longitude")
    loc_description = models.TextField(blank=True)
    vanished = models.ForeignKey(Vanished, on_delete=models.CASCADE)

    def _str__(self):
        return Vanished.first_name + Vanished.last_name