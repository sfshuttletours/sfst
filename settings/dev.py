# this is an extremely simple Satchmo standalone store.

import logging
import os, os.path

from settings.common import INSTALLED_APPS, MIDDLEWARE_CLASSES


DEBUG = True
TEMPLATE_DEBUG = DEBUG

IS_DEV = True

INTERNAL_IPS = ('127.0.0.1',)

DIRNAME = os.path.dirname(os.path.abspath(__file__))

SATCHMO_DIRNAME = DIRNAME

#These are used when loading the test data
SITE_NAME = "simple"

# INSTALLED_APPS = tuple([x for x in INSTALLED_APPS] + ['debug_toolbar'])
# MIDDLEWARE_CLASSES = tuple([x for x in MIDDLEWARE_CLASSES] + ['debug_toolbar.middleware.DebugToolbarMiddleware'])

#These are used when loading the test data
SITE_DOMAIN = "localhost:8000"
SITE_NAME = "Simple Satchmo"

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
CACHE_BACKEND = "locmem:///"
CACHE_PREFIX = "Z"

ACCOUNT_ACTIVATION_DAYS = 7

#Configure logging
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.getLogger('l10n').setLevel(logging.INFO)
logging.info("Satchmo Started")

# email stuff
# EMAIL_BACKEND = 'common.backends.TestingEmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL='info-dev@sfshuttletours.com'
DEFAULT_TO_EMAIL='sfst-dev@tivix.com'

BING_ACCOUNT = "hoangbaodang"
BING_PASS = "danny123"
BING_TOKEN = "BBD37VB98"

try:
    from local import *
except ImportError:
    pass
