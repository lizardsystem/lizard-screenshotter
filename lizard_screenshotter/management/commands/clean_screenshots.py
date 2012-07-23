import shutil
import os
import sys

from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings

from lizard_screenshotter import models


class Command(BaseCommand):
    args = ''
    help = ("Deletes all screenshots from the system")

    def handle(self, *args, **options):
        captures_dir = os.path.join(
            settings.BUILDOUT_DIR, 
            "var", 
            "media", 
            "captures",
        )
        print "Deleting " + str(len([name for name in os.listdir(captures_dir)])) + " screen capture files from disk and database..."
        for root, dirs, files in os.walk(captures_dir):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

        for screenshot in models.Screenshot.objects.all():
            screenshot.delete()