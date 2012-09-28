# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from lizard_screenshotter.views import HomeView
from lizard_screenshotter.views import DirectImageView
from lizard_screenshotter.views import ArchiveView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomeView),
    url(r'^archive/$', ArchiveView),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/', include('lizard_map.urls')),

    url(r'^s/(?P<width>[\d]+)x(?P<height>[\d]+)/(?P<url>.+)/$', DirectImageView),

    url(r'^ui/', include('lizard_ui.urls')),
    )
urlpatterns += debugmode_urlpatterns()
