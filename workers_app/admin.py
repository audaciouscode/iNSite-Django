from django.contrib.gis import admin

from .models import Worker, WorkerDetail

@admin.register(Worker)
class WorkerAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'last_location', 'tags',)
    list_filter = ('tags',)
    search_fields = ['name', 'tags']
    
    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/lib/OpenLayers.js'

@admin.register(WorkerDetail)
class WorkerDetailAdmin(admin.OSMGeoAdmin):
    list_display = ('worker', 'name', 'value', 'priority', 'type')
    list_filter = ('name', 'type', 'priority',)
    search_fields = ['name', 'value']

    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/lib/OpenLayers.js'
