from django.contrib.gis import admin

from .models import SitePlan, PlanDetail, PlanOverlay, AreaOfInterest, MediaAttachment

@admin.register(SitePlan)
class SitePlanAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'location',)
    search_fields = ['name']

    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/lib/OpenLayers.js'

@admin.register(PlanDetail)
class PlanDetailAdmin(admin.OSMGeoAdmin):
    list_display = ('plan', 'name', 'priority',)
    list_filter = ('plan', 'name', 'priority', 'type',)
    search_fields = ['name', 'value', 'type']

    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/lib/OpenLayers.js'

@admin.register(PlanOverlay)
class PlanOverlayAdmin(admin.OSMGeoAdmin):
    list_display = ('plan', 'name', 'z_index', 'center_point', 'scale', 'rotation',)
    list_filter = ('plan', 'z_index',)
    search_fields = ['name']

    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/lib/OpenLayers.js'

@admin.register(AreaOfInterest)
class AreaOfInterestAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'overlay', 'location', 'is_point', 'tags', 'created', 'updated')
    list_filter = ('created', 'updated', 'tags',)
    search_fields = ['name']

    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/lib/OpenLayers.js'

@admin.register(MediaAttachment)
class MediaAttachmentAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'mime_type', 'created', 'location',)
    list_filter = ('created', 'mime_type',)
    search_fields = ['name', 'mime_type']

    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/lib/OpenLayers.js'
