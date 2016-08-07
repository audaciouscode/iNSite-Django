from django.core.management import call_command

from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from passive_data_kit.views import add_data_bundle

from .models import PlanOverlay, SitePlan

def map_app_sites_json(request):
    c = RequestContext(request)
    
    sites = []
    
    for plan in SitePlan.objects.all():
        site = {}
        
        site['name'] = plan.name
        site['location'] = plan.location.srid
        site['overlays'] = []
        
        for overlay in plan.overlays.all():
            plan_overlay = {}
            
            plan_overlay['name'] = overlay.name
            plan_overlay['overlay_url'] = 'https://insite.audacious-software.com' + overlay.overlay_background.url
            plan_overlay['overlay_center_x'] = overlay.center_point.x
            plan_overlay['overlay_center_y'] = overlay.center_point.y
            plan_overlay['overlay_scale'] = overlay.scale
            plan_overlay['overlay_rotation'] = overlay.rotation
            plan_overlay['z_index'] = overlay.z_index
            
            points = []
            
            for oai in plan.areas_of_interest.all():
                point = {}
                
                point['id'] = oai.pk
                point['name'] = oai.name
                point['description'] = oai.description
                point['tags'] = oai.tags
                point['update'] = oai.updated.isoformat()
                
                center = oai.location.centroid

                point['latitude'] = center.y
                point['longitude'] = center.x
                
                points.append(point)
                
            plan_overlay['points'] = points
                
            site['overlays'].append(plan_overlay)
            
        sites.append(site)
            
    return JsonResponse(sites, json_dumps_params={ 'indent': 2 }, safe=False)

            
@csrf_exempt
def map_app_upload_json(request):
    response = add_data_bundle(request)
    
    call_command('process_bundles')
    call_command('extract_interest_areas')
    
    return response
