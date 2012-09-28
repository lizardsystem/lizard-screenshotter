# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
from urlparse import urlparse

import os
import subprocess
import time

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token  # required for Ajax post
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.utils import simplejson
from django.views.static import serve


from lizard_screenshotter.models import Screenshot


def HomeView(request):
    """HomeView for the screenshotter."""

    if request.method == 'POST':
        url = str(request.POST.get('url'))
        width = request.POST.get('width')
        height = request.POST.get('height')
        timeout = request.POST.get('timeout')
        element = request.POST.get('element')

        screenshot = process_screenshot(url, width, height, timeout, element)

        return HttpResponse(
            simplejson.dumps({'screenshot': screenshot.screenshotname,
                              'originalurl': url}),
            mimetype='application/json')

    get_token(request)
    return render_to_response(
        "lizard_screenshotter/home.html",
        locals(),
        context_instance=RequestContext(request)
        )


def DirectImageView(request):
    """A Direct image view that returns the image directly."""

    if request.method != 'GET':
        return HttpResponseRedirect('/')

    url = request.GET.get('url')
    width = request.GET.get('width', 1204)
    height = request.GET.get('height', 768)
    timeout = request.GET.get('timeout', '')
    element = request.GET.get('element', '')
    screenshot = process_screenshot(url, width, height, timeout, element)

    return serve(request, screenshot.fullpath, '/')


def process_screenshot(url, width, height, timeout='', element=''):
    """Process the screenshot in a generic way. """

    netloc = urlparse(url).netloc
    screenshotname = str(netloc) + "-" + str(time.time()) + ".png"

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
        timeout,
        element,
    ])

    return Screenshot.objects.create(
        identifier=slugify(url),
        original_url=url,
        fullpath=outputfile,
        screenshotname=screenshotname)
