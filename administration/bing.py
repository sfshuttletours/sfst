from adspygoogle.adwords.AdWordsClient import AdWordsClient
from adspygoogle.common import Utils

import urllib
import os
import os.path
import time
import zipfile

import elementtree.ElementTree as ET
import httplib
from datetime import datetime, timedelta

path = os.path.dirname(__file__)

acctId = 6589338
# cusId = 15036697

# The following is the production host.
host = "adcenterapi.microsoft.com"
bing_env = 0


host = "adcenterapi.microsoft.com"

# The Web service URI, proxy, and service operation definitions.
URI = "https://" + host + "/Api/Advertiser/V8/"
reportProxy = URI + "Reporting/ReportingService.svc?wsdl"

# The version 8 namespace
ns_report = "https://adcenter.microsoft.com/v8"

# Choose a directory and filename where you will download the report
downloadFile = path + '/bing_reports/bing_report.zip'

username = "API_Shuttle"
password = "Pa55w0rd"
developertoken = "000YB7D35H655326"
accountId = "995905"

#NewYork tour
campaignId = "41090427"

#All Wine Country Tour
all_wine_country_tour = "40626940"

#Sanfrancisco tour
sanfran_tour = "40626894"

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year

# The Web service URI, proxy, and service operation definitions.
URI = "https://" + host + "/Api/Advertiser/V8/"
campaignProxy = URI + "CampaignManagement/CampaignManagementService.svc?wsdl"
action = "GetCampaignsByAccountId"

def submitGenerateReport (custom_date_range):
    custom_date_start = datetime.today().date() - timedelta(days=custom_date_range)
    start_day = custom_date_start.day
    start_month = custom_date_start.month
    start_year = custom_date_start.year

    soapStr = """<?xml version="1.0" encoding="utf-8"?>
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
      <s:Header>
        <h:ApplicationToken i:nil="true" xmlns:h="https://adcenter.microsoft.com/v8" xmlns:i="http://www.w3.org/2001/XMLSchema-instance" />
        <h:CustomerAccountId i:nil="true" xmlns:h="https://adcenter.microsoft.com/v8" xmlns:i="http://www.w3.org/2001/XMLSchema-instance" />
        <h:CustomerId i:nil="true" xmlns:h="https://adcenter.microsoft.com/v8" xmlns:i="http://www.w3.org/2001/XMLSchema-instance" />
        <h:DeveloperToken xmlns:h="https://adcenter.microsoft.com/v8">%s</h:DeveloperToken>
        <h:Password xmlns:h="https://adcenter.microsoft.com/v8">%s</h:Password>
        <h:UserName xmlns:h="https://adcenter.microsoft.com/v8">%s</h:UserName>
      </s:Header>
      <s:Body>
        <SubmitGenerateReportRequest xmlns="https://adcenter.microsoft.com/v8">
          <ReportRequest i:type="BudgetSummaryReportRequest" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
            <Format>Xml</Format>
            <Language i:nil="true" />
            <ReportName>My Keyword Performance Report</ReportName>
            <ReturnOnlyCompleteData>false</ReturnOnlyCompleteData>
            <Aggregation>Daily</Aggregation>
            <Columns>
              <BudgetSummaryReportColumn>AccountName</BudgetSummaryReportColumn>
              <BudgetSummaryReportColumn>AccountNumber</BudgetSummaryReportColumn>
              <BudgetSummaryReportColumn>CampaignName</BudgetSummaryReportColumn>
              <BudgetSummaryReportColumn>Date</BudgetSummaryReportColumn>
              <BudgetSummaryReportColumn>CurrencyCode</BudgetSummaryReportColumn>
              <BudgetSummaryReportColumn>MonthlyBudget</BudgetSummaryReportColumn>
              <BudgetSummaryReportColumn>DailySpend</BudgetSummaryReportColumn>
            </Columns>
            <Scope>
              <AccountIds i:nil="false" xmlns:a1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
                <a1:long>%s</a1:long>
              </AccountIds>
            </Scope>
            <Time>
              <CustomDateRangeEnd>
                <Day>%s</Day>
                <Month>%s</Month>
                <Year>%s</Year>
              </CustomDateRangeEnd>
              <CustomDateRangeStart>
                <Day>%s</Day>
                <Month>%s</Month>
                <Year>%s</Year>
              </CustomDateRangeStart>
              <PredefinedTime i:nil="true"></PredefinedTime>
            </Time>
          </ReportRequest>
        </SubmitGenerateReportRequest>
      </s:Body>
    </s:Envelope>""" % (developertoken, password, username, accountId, current_day, current_month, current_year, start_day, start_month, start_year)

    #<PredefinedTime>LastMonth</PredefinedTime>

    # Create the Web service client, and then add the required headers.
    _service = httplib.HTTPS(host)
    _service.putrequest("POST", reportProxy)
    _service.putheader("Accept","text/xml")
    _service.putheader("Accept","multipart/*")
    _service.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    _service.putheader("Content-length", "%d" % len(soapStr))
    _service.putheader("SOAPAction", "SubmitGenerateReport")
    _service.putheader("HOST", str(host))
    _service.endheaders()

    # Execute the Web service request.
    _service.send(soapStr)

    # Get the response message and results.
    statuscode, statusmessage, header = _service.getreply()
    res = _service.getfile().read()

    response = None

    if statusmessage == "OK":

        response = ET.fromstring(res)

    else:

        # The method call failed.
        print soapStr
        print "SubmitGenerateReport failed.\n"
        print "Status Code: ", statuscode, statusmessage, "\n"
        print "Header: ", header, "\n"
        print res

        faultTree = ET.fromstring(res)
        print faultTree.findtext(".//faultcode"), " ", \
            faultTree.findtext(".//faultstring")

    return response if response else None

def pollGenerateReport (reportRequestId):

    soapStr = """<?xml version="1.0" encoding="utf-8"?>
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
      <s:Header>
        <h:ApplicationToken i:nil="true" xmlns:h="https://adcenter.microsoft.com/v8" xmlns:i="http://www.w3.org/2001/XMLSchema-instance" />
        <h:CustomerAccountId i:nil="true" xmlns:h="https://adcenter.microsoft.com/v8" xmlns:i="http://www.w3.org/2001/XMLSchema-instance" />
        <h:CustomerId i:nil="true" xmlns:h="https://adcenter.microsoft.com/v8" xmlns:i="http://www.w3.org/2001/XMLSchema-instance" />
        <h:DeveloperToken xmlns:h="https://adcenter.microsoft.com/v8">%s</h:DeveloperToken>
        <h:Password xmlns:h="https://adcenter.microsoft.com/v8">%s</h:Password>
        <h:UserName xmlns:h="https://adcenter.microsoft.com/v8">%s</h:UserName>
      </s:Header>
      <s:Body>
        <PollGenerateReportRequest xmlns="https://adcenter.microsoft.com/v8">
          <ReportRequestId>%s</ReportRequestId>
        </PollGenerateReportRequest>
      </s:Body>
    </s:Envelope>""" % (developertoken, password, username, reportRequestId)

    # Create the Web service client, and then add the required headers.
    _service = httplib.HTTPS(host)
    _service.putrequest("POST", reportProxy)
    _service.putheader("Accept","text/xml")
    _service.putheader("Accept","multipart/*")
    _service.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    _service.putheader("Content-length", "%d" % len(soapStr))
    _service.putheader("SOAPAction", "PollGenerateReport")
    _service.putheader("HOST", str(host))
    _service.endheaders()

    # Execute the Web service request.
    _service.send(soapStr)

    # Get the response message and results.
    statuscode, statusmessage, header = _service.getreply()
    res = _service.getfile().read()

    response = None

    if statusmessage == "OK":

        response = ET.fromstring(res)

    else:

        # The method call failed.
        print soapStr
        print "PollGenerateReport failed.\n"
        print "Status Code: ", statuscode, "\n"
        print "Header: ", header, "\n"
        print res

        faultTree = ET.fromstring(res)
        print faultTree.findtext(".//faultcode"), " ", \
            faultTree.findtext(".//faultstring")

    return response if response else None

def unzipReport():
    zfile = zipfile.ZipFile(downloadFile)
    for name in zfile.namelist():
      rf = zfile.read(name)
      # import pdb; pdb.set_trace()
    rs = ET.fromstring(rf)

    rows = []
    for ele_row in rs[1]:
      row = {}
      for ele in ele_row:
        tag = ele.tag.replace('{http://adcenter.microsoft.com/advertiser/reporting/v5/XMLSchema}', '')
        row[tag] = ele.get('value')
      rows.append(row)
    return rows

def getBingReport(custom_date_range):
    from datetime import datetime, timedelta
    from cPickle import loads, dumps
    
    cached = {
        'last_updated': datetime.now(),
        'results': [],
        'custom_date_range': custom_date_range
    }
    
    print '===== get_bing_report '
    
    try:
        f = open(path + '/bing_reports/bing.pkl', 'rb')
        cached = loads(f.read())
        f.close()

        if cached['last_updated'] + timedelta(minutes=60) > datetime.now() and cached.get('custom_date_range', 0) >= custom_date_range:
            print '===== loaded report form cache'
            return cached['results']
        else:
            print '===== cache is staled'
    except:
        print '===== cache file does not exist'
    
    response = submitGenerateReport(custom_date_range)
    polling = 0
    waitMinutes = 1

    if response is not None:
        reportRequestId = (response.findall(".//{" + ns_report + "}ReportRequestId"))[0].text
        polling = 1

    while (polling):

        status = None
        response = pollGenerateReport(reportRequestId)
        if response is not None:
            status = (response.findall(".//{" + ns_report + "}Status"))[0].text
            print "Status: %s \n\r" % status

        if (status == "Success"):
            # Get the URL of the report to download.
            downloadUrl = (response.findall(".//{" + ns_report + "}ReportDownloadUrl"))[0].text
            print "Downloading From : %s\n\r" % downloadUrl

            # Make sure that the destination directory exists
            directory = os.path.dirname(downloadFile)
            if not os.path.exists(directory):
                os.makedirs(directory)

            urllib.urlretrieve(downloadUrl, downloadFile)

            print "Report file written to %s.\n\n" % downloadFile

            polling = 0

        if (status != "Pending"):
            polling = 0

        if(polling):
            # Wait a while before getting the status again.
            time.sleep(waitMinutes * 60)
    report = unzipReport()
    
    
    if report:
        f = open(path + '/bing_reports/bing.pkl', 'wb+')
        print 'saved report to cache'
        f.write(dumps({'results': report, 'last_updated': datetime.now(), 'custom_date_range': custom_date_range}))
        f.close()
    # end while
    return report