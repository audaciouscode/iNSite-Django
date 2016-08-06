from django.shortcuts import render_to_response
from django.template import RequestContext

def website_home(request):
    c = RequestContext(request)

    return render_to_response('website_home.html', c)
