from adspygoogle.adwords.AdWordsClient import AdWordsClient
from adspygoogle.common import Utils
import os

import elementtree.ElementTree as ET
import httplib

def adwords_get_reporting():
    client = AdWordsClient(path=os.path.join('282-422-0171', 'leavemealone1', '282-422-0171', '..'))
    campaign_service = client.GetCampaignService(version='[latest_version]')
    budget_service = client.GetBudgetService(version='[latest_version]')

    # Create a budget, which can be shared by multiple campaigns.
    budget = {
        'name': 'Interplanetary budget #%s' % Utils.GetUniqueName(),
        'amount': {
            'microAmount': '50000000'
        },
        'deliveryMethod': 'STANDARD',
        'period': 'DAILY'
    }

    budget_operations = [{
                             'operator': 'ADD',
                             'operand': budget
                         }]

    # Add the budget.
    budget_id = budget_service.Mutate(budget_operations)[0]['value'][0]['budgetId']
    operations = [{
                      'operator': 'ADD',
                      'operand': {
                          'name': 'Interplanetary Cruise #%s' % Utils.GetUniqueName(),
                          'status': 'PAUSED',
                          'biddingStrategyConfiguration': {
                              'biddingStrategyType': 'MANUAL_CPC'
                          },
                          'endDate': '20180101',
                          'budget': {
                              'budgetId': budget_id
                          },
                          'settings': [{
                                           'xsi_type': 'KeywordMatchSetting',
                                           'optIn': 'false'
                                       }]
                      }
                  }]
    campaigns = campaign_service.Mutate(operations)[0]

    # Display results.
    for campaign in campaigns['value']:
        print ('Campaign with name \'%s\' and id \'%s\' was added.'
               % (campaign['name'], campaign['id']))

    print
    print ('Operations: %s operations' % (client.GetOperations()))


# Application-specific value.
acctId = 6589338
# cusId = 15036697

# This example host is for the sandbox environment.
# Update the URL as needed when you use the production environment.
host = "api.sandbox.bingads.microsoft.com"
bing_env = 1
# The following is the production host.
#host = "adcenterapi.microsoft.com"
#bing_env = 0

# The Web service URI, proxy, and service operation definitions.
URI = "https://" + host + "/Api/Advertiser/V8/"
campaignProxy = URI + "CampaignManagement/CampaignManagementService.svc?wsdl"
action = "GetCampaignsByAccountId"

# The namespace definitions.
ns_soapenv = "http://schemas.xmlsoap.org/soap/envelope/"
ns_xsd = "http://www.w3.org/1999/XMLSchema"
ns_xsi = "http://www.w3.org/2001/XMLSchema-instance"
ns_soapenc = "http://schemas.xmlsoap.org/soap/encoding/"
ns_arrays = "http://schemas.microsoft.com/2003/10/Serialization/Arrays"
ns_bingads = "https://adcenter.microsoft.com/v8"
ns_adAPI = "https://adapi.microsoft.com"

# The namespace prefix mappings.
ET._namespace_map[ns_soapenv] = 'SOAP-ENV'
ET._namespace_map[ns_xsd] = 'xsd'
ET._namespace_map[ns_xsi] = 'xsi'
ET._namespace_map[ns_soapenc] = 'SOAP-ENC'

# This method programmatically constructs a SOAP envelope that contains the
# GetCampaignsByAccountId request.
def createSoapRequest(username, password, devtoken):
    # Create the root element.
    root = ET.Element("{" + ns_soapenv + "}Envelope")

    # Create the header element.
    header = ET.SubElement(root, "{" + ns_soapenv + "}Header")
    header.attrib["xmlns"] = ns_bingads

    # Add in the developer token.
    devToken = ET.SubElement(header, "DeveloperToken")
    devToken.text = devtoken

    # Add in the user name.
    userName = ET.SubElement(header, "UserName")
    userName.text = username

    # Add in the password.
    passWord = ET.SubElement(header, "Password")
    passWord.text = password

    # Add in the customer account ID.
    accountId = ET.SubElement(header, "CustomerAccountId")
    accountId.text = str(acctId)

    # Create the body element.
    body = ET.SubElement(root, "{" + ns_soapenv + "}Body")
    body.attrib["xmlns"] = ns_bingads

    # Create the GetCampaignsByAccountIdRequest element.
    getCampaignsByAccountIdRequest = ET.SubElement(body, "GetCampaignsByAccountIdRequest")

    # Add in the account ID.
    accountId = ET.SubElement(getCampaignsByAccountIdRequest, "AccountId")
    accountId.text = str(acctId)

    return root

# Create a Web service client, and then execute the
# GetCampaignsByAccountId method.
def getCampaignsByAccountId(username, password, devtoken):
    soapRequest = createSoapRequest(username, password, devtoken)
    soapStr = ET.tostring(soapRequest)


    # Create the Web service client, and then add the required headers.
    _service = httplib.HTTPS(host)
    _service.putrequest("POST", campaignProxy)
    _service.putheader("Accept", "text/xml")
    _service.putheader("Accept", "multipart/*");
    _service.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    _service.putheader("Content-length", "%d" % len(soapStr))
    _service.putheader("SOAPAction", action)
    _service.putheader("HOST", str(host))
    _service.endheaders()


    # Execute the Web service request.
    _service.send(soapStr)

    # Get the response message and results.
    statuscode, statusmessage, header = _service.getreply()
    res = _service.getfile().read()

    if statusmessage == "OK":

        # The method call was successful.
        print action + " succeeded."
        # Display the tracking ID.
        responseTree = ET.fromstring(res)
        print "Tracking ID: " + responseTree.findtext(".//{" + ns_bingads + "}TrackingId")
        # Print out the campaign information.
        print # Blank line.
        print "The following campaign IDs were returned by " + action + ":"
        #campaignList = responseTree.findall(".//{" + ns_bingads + "}Campaign")

        campaignList = responseTree.findall(".//Campaigns")
        print len(campaignList)
        # for campaign in campaignList:
            # name = campaign.find("{" + ns_bingads + "}Name")
            # description = campaign.find("{" + ns_bingads + "}Description")
            # monthlyBudget = campaign.find("{" + ns_bingads + "}MonthlyBudget")
            # budgetType = campaign.find("{" + ns_bingads + "}BudgetType")
            #
            # print "Name          : ", name.text
            # print "Description   : ", description.text
            # print "MonthlyBudget : ", monthlyBudget.text
            # print "BudgetType    : ", budgetType.text
            # print # Blank line to separate campaigns.

    else:
        # The method call failed.
        print soapStr
        print action + " failed.\n"
        print "Status Code: ", statuscode, statusmessage, "\n"
        print "Header: ", header, "\n"
        print res

        faultTree = ET.fromstring(res)
        print faultTree.findtext(".//faultcode"), " ", \
            faultTree.findtext(".//faultstring")

        # The error received could be either ApiFaultDetail or AdApiFaultDetail.
        if None != faultTree.find(".//{" + ns_adAPI + "}AdApiFaultDetail"):
            #
            print "AdApiFaultDetail exception encountered."
            print "Tracking ID: " + faultTree.findtext(".//{" + ns_adAPI + "}TrackingId")
            # Display AdApiErrors.
            errorList = faultTree.findall(".//{" + ns_adAPI + "}AdApiError")
            for error in errorList:
                message = error.find("{" + ns_adAPI + "}Message")
                detail = error.find("{" + ns_adAPI + "}Detail")
                errorCode = error.find("{" + ns_adAPI + "}ErrorCode")
                code = error.find("{" + ns_adAPI + "}Code")
                print "Error encountered:"
                print "\tMessage   : ", message.text
                print "\tDetail    : ", detail.text
                print "\tErrorCode : ", errorCode.text
                print "\tCode      : ", code.text

        else:
            if None != faultTree.find(".//{" + ns_bingads + "}ApiFaultDetail"):
                print "ApiFaultDetail exception encountered."
                print "Tracking ID: " + faultTree.findtext(".//{" + ns_adAPI + "}TrackingId")

                # Display operation errors.
                operationErrorList = faultTree.findall(".//{" + ns_bingads + "}OperationError")
                for operationError in operationErrorList:
                    message = operationError.find("{" + ns_bingads + "}Message")
                    details = operationError.find("{" + ns_bingads + "}Details")
                    errorCode = operationError.find("{" + ns_bingads + "}ErrorCode")
                    code = operationError.find("{" + ns_bingads + "}Code")
                    print "Operation error encountered:"
                    print "\tMessage   : ", message.text
                    print "\tDetails   : ", details.text
                    print "\tErrorCode : ", errorCode.text
                    print "\tCode      : ", code.text

                # Display batch errors.
                batchErrorList = faultTree.findall(".//{" + ns_bingads + "}BatchError")
                for batchError in batchErrorList:
                    index = batchError.find("{" + ns_bingads + "}Index")
                    message = batchError.find("{" + ns_bingads + "}Message")
                    details = batchError.find("{" + ns_bingads + "}Details")
                    errorCode = batchError.find("{" + ns_bingads + "}ErrorCode")
                    code = batchError.find("{" + ns_bingads + "}Code")
                    print "Batch error encountered for array index ", index.text, "."
                    print "\tMessage   : ", message.text
                    print "\tDetails   : ", details.text
                    print "\tErrorCode : ", errorCode.text
                    print "\tCode      : ", code.text

        print
        print "Response: ", res
    return campaignList