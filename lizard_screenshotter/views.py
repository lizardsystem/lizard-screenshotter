# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
from urlparse import urlparse

# from sorl.thumbnail import get_thumbnail
import os
import subprocess
import threading
import time

from lizard_screenshotter.models import Screenshot

from django.conf import settings
from django.http import HttpResponse
from django.http import Http404
from django.middleware.csrf import get_token #required for Ajax post
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.utils import simplejson
from django.views.static import serve


timeout = 10

class Command(object):
    # From: http://stackoverflow.com/questions/1191374/subprocess-with-timeout
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print 'Thread started'
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            print 'Thread finished'

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()
        print self.process.returncode




def HomeView(request):

    if request.method == 'POST':

        url = str(request.POST.get('url'))
        width = request.POST.get('width')
        height = request.POST.get('height')
        timeout = request.POST.get('timeout')
        element = request.POST.get('element')
        
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
        command = Command("/usr/bin/timeout --kill-after=" + timeout + " " + timeout + " " +
            str(phantomjs) + " " + 
            str(capturejs) + " \"" + 
            str(url) + "\" " + 
            str(outputfile) + " " + 
            str(width) + " " + 
            str(height) + " " + 
            str(timeout) + " " + 
            str(element))
        command.run(timeout=15)

        screenshot = Screenshot()
        screenshot.identifier = slugify(url)
        screenshot.original_url = url
        screenshot.fullpath = outputfile
        screenshot.screenshotname = screenshotname
        screenshot.save()

        return HttpResponse(simplejson.dumps({'screenshot':screenshotname, 'originalurl':url}), mimetype='application/json')
    else:
        get_token(request)
        return render_to_response(
            "lizard_screenshotter/home.html",
            locals(), 
            context_instance=RequestContext(request)
        )
        
        
def DirectImageView(request, width, height, url):
    # im = get_thumbnail(my_file, width+'x'+height, crop='center', quality=99)
    print "width: " + str(width)
    print "height: " + str(height)
    print "url: "+ str(url)
    import pprint
    pprint.pprint(request.GET)
    if request.GET:
        url = url + "?" + request.GET.urlencode()
    
    element = str("")
    timeout = str(2000)

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
    command = Command("/usr/bin/timeout --kill-after=" + timeout + " " + timeout + " " +
        str(phantomjs) + " " + 
        str(capturejs) + " \"" + 
        str(url) + "\" " + 
        str(outputfile) + " " + 
        str(width) + " " + 
        str(height) + " " + 
        str(timeout) + " " + 
        str(element))
    command.run(timeout=15)
    # subprocess.call([
    #     phantomjs, 
    #     capturejs, 
    #     url, 
    #     outputfile, 
    #     width, 
    #     height,
    #     timeout,
    #     element,
    # ])
    screenshot = Screenshot()
    screenshot.identifier = slugify(url)
    screenshot.original_url = url
    screenshot.fullpath = outputfile
    screenshot.screenshotname = screenshotname
    screenshot.save()
    # im = get_thumbnail(outputfile, width+'x'+height, crop='center', quality=99)
    # return HttpResponse(outputfile.r, mimetype="image/png")
    return serve(request, outputfile, '/')
        
        
        
        
def ArchiveView(request):
    raise Http404
    # screenshots = Screenshot.objects.order_by('-id')[:100]
    # return render_to_response(
    #     "lizard_screenshotter/archive.html", 
    #     locals(),
    #     context_instance=RequestContext(request)
    # )