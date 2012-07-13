from lizard_screenshotter.settings import *

DATABASES = {
    # Changed server from production to staging
    'default': {
        'NAME': 'lizard_screenshotter',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'lizard_screenshotter',
        'PASSWORD': '-7ci)%g9*#',
        'HOST': 's-web-db-00-d03.external-nens.local',
        'PORT': '5432',
        },
    }

# TODO: add staging gauges ID here.
UI_GAUGES_SITE_ID = ''  # Staging has a separate one.
