# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
from urlparse import urlparse

import os
import subprocess
import time

from lizard_screenshotter.models import Screenshot
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.static import serve


def HomeView(request):

    if request.method == 'POST':

        url = request.POST.get('url')
        width = request.POST.get('width')
        height = request.POST.get('height')
        timeout = request.POST.get('timeout')
        
        o = urlparse(url)

        screenshotname = str(o.netloc) + "-" + str(time.time()) + ".png"

        phantomjs = os.path.join(settings.BUILDOUT_DIR, "bin", "phantomjs")
        capturejs = os.path.join(settings.BUILDOUT_DIR, "capture.js")
        outputfile = os.path.join(
            settings.BUILDOUT_DIR, 
            "var", 
            "media", 
            "captures", 
            screenshotname
        )
        subprocess.call([
            phantomjs, 
            capturejs, 
            url, 
            outputfile, 
            width, 
            height,
            timeout
        ])

        screenshot = Screenshot()
        screenshot.fullpath = outputfile
        screenshot.screenshotname = screenshotname
        screenshot.save()

        return serve(request, outputfile, '/')
    else:
        return render_to_response(
            "lizard_screenshotter/home.html",
            locals(), 
            context_instance=RequestContext(request)
        )
        
        
        
def ArchiveView(request):
    screenshots = Screenshot.objects.order_by('-id')[:25]
    return render_to_response(
        "lizard_screenshotter/archive.html", 
        locals(),
        context_instance=RequestContext(request)
    )