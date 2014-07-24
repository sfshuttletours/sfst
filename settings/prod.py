# PROD overrides for Django settings

DEBUG = False

IS_PROD = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sfst',
        'USER': 'root',
        'PASSWORD': 'sfst-rules',
        'HOST': 'localhost',
        'OPTIONS': {'init_command' : 'SET NAMES "utf8", storage_engine=INNODB',},
    },
    'legacy': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/sfst/work/sfst/src/sfst/SFS.db',
    }
}

SITE_DOMAIN = 'booking.sanfranshuttletours.com'

# email stuff
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'common.backends.SFSTEmailBackend'
DEFAULT_FROM_EMAIL='info@sfshuttletours.com'
DEFAULT_TO_EMAIL='info@sfshuttletours.com'


# Temporary override using Tivix sendgrid credentials
# Email settings #
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sumit@tivix.com'
EMAIL_HOST_PASSWORD = 'tivix-rules'
EMAIL_USE_TLS = True


CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

SATCHMO_SETTINGS = {
    'SHOP_BASE' : '',
    'MULTISHOP' : False,
    'SSL': True
}

# Force SSL protocol for the whole site
FORCE_SSL = True
