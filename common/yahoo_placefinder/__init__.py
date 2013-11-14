import urllib2

from django.conf import settings


YAHOO_URL = "http://where.yahooapis.com/v1/places.q('%s')?appid=%s&format=json"


def get_location_details(zip_code):
    APP_ID = getattr(settings, 'YAHOO_APP_ID', '')
    data = urllib2.urlopen(YAHOO_URL % (zip_code, APP_ID)).read()
    return data
