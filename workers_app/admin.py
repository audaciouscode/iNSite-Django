from django.contrib import admin

from .models import Worker, WorkerDetail

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_location', 'tags',)
    list_filter = ('tags',)
    search_fields = ['name', 'tags']

@admin.register(WorkerDetail)
class WorkerDetailAdmin(admin.ModelAdmin):
    list_display = ('worker', 'name', 'value', 'priority', 'type')
    list_filter = ('name', 'type', 'priority',)
    search_fields = ['name', 'value']
