"""
WSGI config for blah project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Kraggne_test.settings")

DOC_ROOT = os.path.realpath(os.path.join(\
        os.path.dirname(os.path.abspath(__file__)), '../'))

PYTHONPATH = [DOC_ROOT, os.path.join(DOC_ROOT, 'Kraggne_test')]

SRC_PATH = os.path.join(DOC_ROOT, 'src/')
for l in os.listdir(SRC_PATH):
    p = os.path.join(SRC_PATH, l)
    if os.path.isdir(p) and os.path.exists(os.path.join(p, 'setup.py')):
        PYTHONPATH.append(p)

EGGS_PATH = os.path.join(DOC_ROOT, '.duke/eggs/')
for l in os.listdir(EGGS_PATH):
    p = os.path.join(EGGS_PATH, l)
    if os.path.isdir(p) and p.endswith('.egg'):
        PYTHONPATH.append(p)

sys.path[0:0] = PYTHONPATH

import Kraggne_test

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
