from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField

class Worker(models.Model):
    name = models.CharField(max_length=1024)
    tags = ArrayField(models.CharField(max_length=256))

    secret = models.CharField(max_length=1024)
    
    def location_history(self):
        return  []

    def last_location(self):
        return None
    
class WorkerDetail(models.Model):
    worker = models.ForeignKey(Worker, related_name='details')
    
    name = models.CharField(max_length=1024)
    value = models.TextField(max_length=1048576)
    
    priority = models.IntegerField(default=0)
    type = models.CharField(max_length=1024, default='text')
