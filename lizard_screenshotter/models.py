# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
from django.db import models
import datetime


class Screenshot(models.Model):
    """(Screenshot description)"""
    created_on = models.DateTimeField(blank=False, default=datetime.datetime.now)
    fullpath = models.CharField(blank=False, max_length=255)
    screenshotname = models.CharField(blank=False, max_length=255)
    

    def __unicode__(self):
        return u"Screenshot"
