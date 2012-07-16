# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals

from django.contrib import admin

from lizard_screenshotter import models


admin.site.register(models.Screenshot)
