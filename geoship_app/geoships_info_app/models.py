from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Vessel(models.Model):
    date = models.DateTimeField(default=now)
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.code)


class History(models.Model):
    vessel = models.ForeignKey("geoships_info_app.Vessel", on_delete=models.CASCADE, related_name='history', blank=True, null=True)
    date = models.DateTimeField(default=now)
    geo_date = models.DateTimeField()
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.vessel.name
