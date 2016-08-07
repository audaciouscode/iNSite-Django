 # -*- coding: utf-8 -*-

import datetime
import json
import os
import pytz
import traceback

import importlib

from zipfile import ZipFile

from django.conf import settings
from django.core.files import File
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from django.contrib.gis.geos import Polygon
from django.template.loader import render_to_string
from django.utils import timezone

from passive_data_kit.decorators import handle_lock
from passive_data_kit.models import DataPoint

from map_app.models import AreaOfInterest, SitePlan

class Command(BaseCommand):
    help = 'Extracts areas of interest from DataPoint objects.'

    def add_arguments(self, parser):
        pass
#        parser.add_argument('--delete',
#            action='store_true',
#            dest='delete',
#            default=False,
#            help='Delete data bundles after processing')
#
#        parser.add_argument('--count', 
#            type=int, 
#            dest='bundle_count',
#            default=100,
#            help='Number of bundles to process in a single run')
    
    @handle_lock
    def handle(self, *args, **options):
        os.umask(000)
        
        pending = DataPoint.objects.filter(generator_identifier='insite_report').exclude(properties__contains={'insite_processed': True})
        
        for item in pending:
            aoi = AreaOfInterest(name=item.properties['description'])
            
            aoi.overlay = SitePlan.objects.all()[0]

            aoi.is_point = True
            aoi.tags = item.properties['tags']
            aoi.description = item.properties['description']
            aoi.created = item.created
            aoi.updated = item.recorded
        
            latitude = item.properties['latitude'];
            longitude = item.properties['longitude'];
            
            aoi.location = Polygon(((longitude, latitude), (longitude - 0.00001, latitude), (longitude - 0.00001, latitude - 0.00001), (longitude, latitude - 0.00001), (longitude, latitude)))
            aoi.save()
        
            item.properties['insite_processed'] = True
            item.save()
    


            

                            
                
            
