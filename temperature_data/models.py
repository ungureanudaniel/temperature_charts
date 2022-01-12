from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import date
import datetime

class Device(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

class DataInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)
    time = models.TimeField()
    devices = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits = 5, decimal_places = 2)

    def get_absolute_url(self):
        return "/data_input/{}".format(self.slug)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # def __unicode__(self):
    #     return unicode(self.devices, 'utf-8')
    def __str__(self):
        return str(self.date) + str(self.time)
