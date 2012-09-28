# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from lizard_screenshotter.views import (
    DirectImageView, HomeView)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomeView),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^s/$',
        DirectImageView),
    )
urlpatterns += debugmode_urlpatterns()
