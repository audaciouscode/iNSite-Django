from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class MediaAttachment(models.Model):
    name = models.CharField(max_length=4096)
    mime_type = models.CharField(max_length=1024)
    content_file = models.FileField(upload_to='plan_overlays')
    
    location = models.PolygonField(null=True)
    created = models.DateTimeField()

class SitePlan(models.Model):
    name = models.CharField(max_length=4096)
        
    location = models.MultiPolygonField(null=True)

class PlanDetail(models.Model):
    plan = models.ForeignKey(SitePlan, related_name='details')
    
    name = models.CharField(max_length=1024)
    value = models.TextField(max_length=1048576)
    
    priority = models.IntegerField(default=0)
    type = models.CharField(max_length=1024, default='text')

class PlanOverlay(models.Model):
    plan = models.ForeignKey(SitePlan, related_name='overlays')
    
    name = models.CharField(max_length=1024)
    overlay_background = models.FileField(upload_to='plan_overlays')
    
    center_point = models.PointField()
    scale = models.FloatField(default=1.0)
    rotation = models.FloatField(default=0.0)
    
    z_index = models.FloatField(default=1.0)
    
class AreaOfInterest(models.Model):
    name = models.CharField(max_length=4096)

    overlay = models.ForeignKey(SitePlan, related_name='areas_of_interest')

    location = models.PolygonField(null=True)
    is_point = models.BooleanField(default=True)
    
    tags = ArrayField(models.CharField(max_length=256))
    
    description = models.TextField(max_length=4194304, null=True, blank=True)
    
    attachments = models.ManyToManyField(MediaAttachment, related_name='attachments')
    
    created = models.DateTimeField()
    updated = models.DateTimeField()
    
    permissions = JSONField(default=[])
