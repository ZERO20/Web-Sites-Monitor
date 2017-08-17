#encoding: utf-8
from django.db import models

# Create your models here.
class Configuration(models.Model):
    url = models.CharField(max_length=200)
    frequency = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'

    def __str__(self):
        return "{} - {} Sec.".format(self.url, self.frequency)


class Monitoring(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)
    url = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Monitoring'
        verbose_name_plural = 'Monitoring'

    def __str__(self):
        return "{} - {} - {}".format(self.status, self.url, self.create_date)