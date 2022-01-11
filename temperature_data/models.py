from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

class DataInput(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date = models.DateTimeField()
    time = models.TimeField()
    devices = models.ForeignKey(Device, related_name='Dispozitive', on_delete=models.CASCADE)
    temp = models.IntegerField()

    def get_absolute_url(self):
        return "/data_input/{}".format(self.slug)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.devices
