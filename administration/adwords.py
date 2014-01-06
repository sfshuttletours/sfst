from adspygoogle.adwords.AdWordsClient import AdWordsClient
from adspygoogle.common import Utils

import urllib
import os
import os.path
import time
import zipfile
import sys

import elementtree.ElementTree as ET
import httplib

from datetime import datetime, timedelta
from adspygoogle import AdWordsClient

path = os.path.dirname(__file__)
download_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'adwords_reports'))

file_list = ['San Francisco Tours.xml', 'ALL Wine Country Tours.xml', 'New York Tours.xml']
customer_list = [{'campaign':'San Francisco Tours', 'pkl_file_name':'adwords_api_auth2.pkl'},
                 {'campaign':'ALL Wine Country Tours', 'pkl_file_name':'adwords_api_auth.pkl'},
                 {'campaign':'New York Tours', 'pkl_file_name':'adwords_api_auth3.pkl'}]


def get_adwords_report(force_update=False):
    # checking if we have the report for the requested period
    
    from datetime import datetime, timedelta
    from cPickle import loads, dumps
    
    cached = {
        'last_updated': datetime.now(),
        'results': [] 
    }
    
    print '===== get_adwords_report '
    
    try:
        f = open( path + '/adwords_reports/adwords.pkl', 'rb')
        cached = loads(f.read())
        f.close()
        
        if not force_update and cached['last_updated'] + timedelta(minutes=60) > datetime.now():
            print '===== loaded report form cache'
            return cached['results']
        else:
            print '===== cache is staled'
    except:
        print '===== cache file does not exist'
     
    download_reports()
    results = []
    
    for file_name in file_list:
        full_file_name = path + '/adwords_reports/' + file_name
        f = open(full_file_name, 'rb')
        et = ET.fromstring(f.read())
        for result in et[:3][2]:
            try:
                results.append({'cost': result.attrib.get('cost').replace(',', ''),
                                'date': datetime.strptime(result.attrib.get('day'),'%Y-%m-%d').strftime('%m/%d/%Y'),
                                'campaign': result.attrib.get('campaign') })
            except:
                pass

    if results:
        f = open(path + '/adwords_reports/adwords.pkl', 'wb+')
        print 'saved report to cache'
        f.write(dumps({'results': results, 'last_updated': datetime.now()}))
        f.close()
        
    return results

def main(client, path):
  # Initialize appropriate service.
  report_downloader = client.GetReportDownloader(version='v201309')

  # Create report definition.
  report = {
      'reportName': 'CRITERIA_PERFORMANCE_REPORT',
      'dateRangeType': 'ALL_TIME',
      'reportType': 'CAMPAIGN_PERFORMANCE_REPORT',
      'downloadFormat': 'XML',
      'selector': {
          'fields': ['CampaignName','CampaignId', 'Cost', 'Date']
      },
      # Enable to get rows with zero impressions.
      'includeZeroImpressions': 'false'
  }

  file_path = report_downloader.DownloadReport(report, file_path=path)

  print 'Report was downloaded to \'%s\'.' % file_path


def download_reports():
  # Initialize client object.
  for customer in customer_list:
    AdWordsClient.auth_pkl_name = customer['pkl_file_name']
    full_path = download_path + '/' + customer['campaign'] + '.xml'
    test_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..')
    client = AdWordsClient(path=test_path)
    main(client, full_path)
