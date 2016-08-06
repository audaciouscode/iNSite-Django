from django.contrib import admin

from .models import SitePlan, PlanDetail, PlanOverlay, AreaOfInterest, MediaAttachment

@admin.register(SitePlan)
class SitePlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    search_fields = ['name']

@admin.register(PlanDetail)
class PlanDetailAdmin(admin.ModelAdmin):
    list_display = ('plan', 'name', 'priority',)
    list_filter = ('plan', 'name', 'priority', 'type',)
    search_fields = ['name', 'value', 'type']

@admin.register(PlanOverlay)
class PlanOverlayAdmin(admin.ModelAdmin):
    list_display = ('plan', 'name', 'z_index', 'center_point', 'scale', 'rotation',)
    list_filter = ('plan', 'z_index',)
    search_fields = ['name']

@admin.register(AreaOfInterest)
class AreaOfInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'overlay', 'location', 'is_point', 'tags', 'created', 'updated')
    list_filter = ('created', 'updated', 'tags',)
    search_fields = ['name']

@admin.register(MediaAttachment)
class MediaAttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mime_type', 'created', 'location',)
    list_filter = ('created', 'mime_type',)
    search_fields = ['name', 'mime_type']
