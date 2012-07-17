from lizard_screenshotter.settings import *

DATABASES = {
    # Changed server from production to staging
    'default': {
        'NAME': os.path.join(BUILDOUT_DIR, 'var', 'sqlite', 'django.db'),
        'ENGINE': 'django.db.backends.sqlite3',
        },
    }

# TODO: add staging gauges ID here.
UI_GAUGES_SITE_ID = ''  # Staging has a separate one.
