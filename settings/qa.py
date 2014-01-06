# QA overrides for Django settings

DEBUG = False 

IS_QA = True

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

SITE_DOMAIN = 'qa.securebookingshuttletours.com'

BING_ACCOUNT = "hoangbaodang"
BING_PASS = "danny123"
BING_TOKEN = "BBD37VB98"

# email stuff
EMAIL_BACKEND = 'common.backends.TestingEmailBackend'
DEFAULT_FROM_EMAIL='info-qa@sfshuttletours.com'
DEFAULT_TO_EMAIL='sfst@tivix.com'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
