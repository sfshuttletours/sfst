import os
import sys
import logging


DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_HASH = '63'

# directory of the project
DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, DIRNAME + '/')
sys.path.insert(0, '/home/vb/danny_projects/sfst/sfst')
sys.path.insert(0, '/home/vb/danny_projects/sfst/sfst/apps')

DJANGO_PROJECT = 'sfst'
DJANGO_SETTINGS_MODULE = 'sfst.settings'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

IS_DEV = False
IS_QA = False
IS_PROD = False

ADMINS = (
     ('SFST', 'sfst-dev@tivix.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sfst',
        'USER': 'root',
        'PASSWORD': 'root123',
        'OPTIONS': {'init_command' : 'SET NAMES "utf8", storage_engine=INNODB',},
    },
    'legacy': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DIRNAME, 'SFS.db'),
    }
}
DATABASE_ROUTERS = ['legacy.router.MyAppRouter',]

TIME_ZONE = 'US/Pacific'
LANGUAGE_CODE = 'en-us'

gettext_noop = lambda s:s
LANGUAGES = (
   ('en', gettext_noop('English')),
)


SITE_ID = 1

MEDIA_ROOT = os.path.join(DIRNAME, 'static/')
MEDIA_URL="/static/"
ADMIN_MEDIA_PREFIX = '/admin_media/'
FIXTURE_DIRS = (
    os.path.join(DIRNAME, 'fixtures'),
)
# Make this unique, and don't share it with anybody.
# SECRET_KEY = '*h&yl3sw26g()u+_fnfz^gq8%fkhp!rhgif0ygt0atfg&344%v'
SECRET_KEY = 'supercalifragilisticexpealidocious' # I think this is the old one

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'django.middleware.transaction.TransactionMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.doc.XViewMiddleware",

    "threaded_multihost.middleware.ThreadLocalMiddleware",

    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    'pagination.middleware.PaginationMiddleware',

    'common.minidetector.Middleware',

    "localsite.middleware.AffiliateMiddleware",
    "localsite.middleware.SNIMiddleware",
    "localsite.middleware.CheckoutMiddleware",
    "localsite.middleware.SiteSkinMiddleware",
    #"satchmo_ext.recentlist.middleware.RecentProductMiddleware",
    #'djangologging.middleware.LoggingMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

#this is used to add additional config variables to each request
# NOTE: If you enable the recent_products context_processor, you MUST have the
# 'satchmo_ext.recentlist' app installed.
TEMPLATE_CONTEXT_PROCESSORS = (
                               'satchmo_store.shop.context_processors.settings',
                               'django.core.context_processors.auth',
                               'django.core.context_processors.media',
                               'django.core.context_processors.request',
                               'django.contrib.messages.context_processors.messages',

                               'common.minidetector.context_processors.is_mobile',

                               'localsite.context_processors.concierge',
                               'localsite.context_processors.affilate',
                               'localsite.context_processors.satchmo_cart_tours',
                               'localsite.context_processors.site_skin',
                               'localsite.context_processors.skins',
                               #'satchmo_ext.recentlist.context_processors.recent_products',
                               )

ROOT_URLCONF = 'sfst.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.humanize',
    'satchmo_store.shop',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.databrowse',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'registration',
    'sorl.thumbnail',
    'keyedcache',
    'livesettings',
    'l10n',
    'satchmo_utils.thumbnail',
    'satchmo_store.contact',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    #'satchmo_store.contact.supplier',
    #'shipping.modules.tiered',
    #'satchmo_ext.newsletter',
    #'satchmo_ext.recentlist',
    #'testimonials',
    'product',
    'product.modules.configurable',
    'product.modules.custom',
    'product.modules.downloadable',
    #'product.modules.subscription',
    #'satchmo_ext.product_feeds',
    #'satchmo_ext.brand',
    'payment',
    # 'payment.modules.dummy',
    'payment.modules.authorizenet',
    # to enable paypal payment uncomment line below
    #'payment.modules.paypal',
    #'payment.modules.giftcertificate',
    #'satchmo_ext.wishlist',
    #'satchmo_ext.upsell',
    #'satchmo_ext.productratings',
    'satchmo_ext.satchmo_toolbar',
    'satchmo_utils',
    'south',
    #'shipping.modules.tieredquantity',
    #'satchmo_ext.tieredpricing',
    #'typogrify',
    # 'debug_toolbar',
    'pagination',
    'app_plugins',
    'django_common',

    'adjustments',
    'administration',
    'concierges',
    'localsite',
    'resellers',
    'common.cron',

    'sentry',
    'raven.contrib.django',
)

CACHE_TIMEOUT = 30 * 60 # 30 minutes?
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

AUTHENTICATION_BACKENDS = (
    'satchmo_store.accounts.email-auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

DEBUG_TOOLBAR_CONFIG = {
   'INTERCEPT_REDIRECTS' : False,
}

#### Satchmo unique variables ####
#from django.conf.urls.defaults import patterns, include
SATCHMO_SETTINGS = {
    'SHOP_BASE' : '',
    'MULTISHOP' : False,
    #'SHOP_URLS' : patterns('satchmo_store.shop.views',)
}

SKIP_SOUTH_TESTS=True

#Configure logging
LOGFILE = '%s/logs/sfst.log' % DIRNAME
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(DIRNAME,LOGFILE),
                    filemode='w')

#------------------
# django-pagination
#------------------
PAGINATION_DEFAULT_PAGINATION = 20
PAGINATION_DEFAULT_WINDOW = 3

#--------------------
# Twilio API settings
#--------------------
TWILIO_ACCOUNT_SID = 'AC6b1d75c7e04bd5a2a21ff1cdb4b9f625'
TWILIO_AUTH_TOKEN = '8775b1fd8900557582f03d15c184c703'
TWILIO_CALLER_ID = '4155135400'

YAHOO_APP_ID = 'TxxPgB3V34FCgS4789bxmLtpWNjw24JO8KvtOt4.EHhBxxiPkIH8Zm9asIbj_i9n9ob_YL8-'
