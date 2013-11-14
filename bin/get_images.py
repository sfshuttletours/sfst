import os
import re
import urllib

from django.conf import settings

base_url = 'http://www.sanfranshuttletours.com/'
url = 'http://www.sanfranshuttletours.com/'
f = urllib.urlopen(url)
source = f.read()
matches = re.findall('''(images/[^"']+)''', source)
for m in matches:
    local_path = os.path.join(settings.MEDIA_ROOT, m)
    if not os.access(local_path, os.R_OK):
        print 'Download %s...' % m
        urllib.urlretrieve(base_url + m, local_path)
