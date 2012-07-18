# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
from django.db import models
import datetime


class Screenshot(models.Model):
    """(Screenshot description)"""
    created_on = models.DateTimeField(blank=False, default=datetime.datetime.now)
    identifier = models.CharField(blank=False, max_length=255)
    original_url = models.CharField(blank=False, max_length=255)
    fullpath = models.CharField(blank=False, max_length=255)
    screenshotname = models.CharField(blank=False, max_length=255)

    def __unicode__(self):
        return str(self.original_url)
