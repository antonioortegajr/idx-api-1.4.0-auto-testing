from apiCall import main
import json

def crudMethods(rootUrl, data, headers):
    componant = '/leads'

    #test lead methods
    endPoint = '/lead'
    url = rootUrl + componant + endPoint
    add = "q"
    add = add + 'w'

    #use all available parametors
    data = 'firstName=Bau&lastName=kim&email=kim.bau.bau.kim%40gmail.com&email2=kim.bau.bau2.kim%40gmail.com&password=password&address=123+fake&city=fake&stateProvince=OR&country=usa&zipCode=HTML&disabled=n&canLogin=y&receiveUpdates=y&flag=y&phone=1234567890&agentOwner=1'

    #Create Lead
    method ='PUT'
    newLeadID = ''
    newLeadReturn = main(url, headers, method, data)
    #sample return {"newID":39}
    print newLeadReturn

    #check for an error
    if (newLeadReturn == 'ERROR'):
        print 'There was an ERROR. Check the errors.text file'

    else:

        #now that we have a lead ID check create and update
        newLeadID = json.loads(newLeadReturn)
        createdLead = str(newLeadID['newID'])
        print createdLead

        #Read Leads
        method ='GET'
        endPoint = '/lead' + createdLead
        main(url, headers, method, data)


        #Update Lead
        method = 'POST'
        url = url + '/' + createdLead

        #test lead methods

        data = 'firstName=Bau2&lastName=kim2&email=kim.bau.bau.kim2%40gmail.com&email2=kim.bau.bau2.kim2%40gmail.com&password=password2&address=1232+fake&city=fake2&stateProvince=OR2&country=usa2&zipCode=22222&disabled=y&canLogin=n&receiveUpdates=n&flag=7&phone=222222220&agentOwner=0'
        updateLeadReturn = main(url, headers, method, data)

        #Delete
        url = url
        method = 'DELETE'
        deleteSearchReturn = main(url, headers, method, data)
        print deleteSearchReturn

addOn = 'lmnop'
#only json works
output = 'json'
key = 'Wb6IHM-GT71Htdd-7rvN-_'
#apiversion = '1.4.0'

#default domain and headers
#rootUrl = 'https://api.idxbroker.com'
rootUrl = 'https://api.idxsandbox.com'

versions = ['1.0.4', '1.1.1', '1.2.0', '1.2.1', '1.2.2', '1.2.0', '1.3.0', '1.4.0']
#versions = ['1.4.0']


data = '';
for version in versions:
    headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":version, "outputtype":output}
    crudMethods(rootUrl, data, headers)
