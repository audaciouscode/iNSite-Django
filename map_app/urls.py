from django.conf.urls import url

from .views import map_app_sites_json, map_app_upload_json

urlpatterns = [
    url(r'^sites.json$', map_app_sites_json, name='map_app_sites_json'),
    url(r'^upload.json$', map_app_upload_json, name='map_app_upload_json'),
]
