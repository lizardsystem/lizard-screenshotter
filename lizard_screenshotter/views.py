# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
import time
import os
import subprocess
from urlparse import urlparse
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

def HomeView(request):

    if request.method == 'POST':

        url = request.POST.get('url')
        width = request.POST.get('width')
        height = request.POST.get('height')
        
        o = urlparse(url)

        phantomjs = os.path.join(settings.BUILDOUT_DIR, "bin", "phantomjs")
        capturejs = os.path.join(settings.BUILDOUT_DIR, "capture.js")
        outputfile = os.path.join(
            settings.BUILDOUT_DIR, 
            "var", 
            "media", 
            "captures", 
            str(o.netloc) + "-" + str(time.time()) + ".png"
        )
        subprocess.call([
            phantomjs, 
            capturejs, 
            url, 
            outputfile, 
            width, 
            height
        ])

        return HttpResponse("png here")
    else:
        return render_to_response("lizard_screenshotter/home.html", locals(), context_instance=RequestContext(request))
