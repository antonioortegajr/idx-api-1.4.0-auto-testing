from apiCall import main
import json

def crudMethods(rootUrl, data, headers):
    componant = '/leads'

    #test lead methods
    endPoint = '/lead'
    url = rootUrl + componant + endPoint
    #Create Lead
    method ='PUT'
    newLeadID = ''

    # numbers each time this function is called
    add = '1234567890';
    putFirstName = 'Bau'+ add
    putLastName = 'kim' + add
    putEmail = 'kim.bau.bau.kim' + add + '%40gmail.com'

    #use all available parametors
    data = 'firstName=' + putFirstName +'&lastName=' + putLastName + '&email=' + putEmail + '&email2=kim.bau.bau2.kim%40gmail.com&password=password&address=123+fake&city=fake&stateProvince=OR&country=usa&zipCode=HTML&disabled=n&canLogin=y&receiveUpdates=y&flag=y&phone=1234567890&agentOwner=1'

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
        data = ''
        add2 = '3' + createdLead
        data = 'firstName=Johnnny'+ add2 +'&lastName=Doe'+ add2 +'&email=johnDoe'+ add2 +'%40gmail.com&email2=johnDoe'+ add2 +'%40gmail.com&password=password'+ add2 +'&address=1232+fake'+ add2 +'&city=fake'+ add2 +'&stateProvince=OR'+ add2 +'&country=usa'+ add2 +'&zipCode=222'+ add2 +'&disabled=y&canLogin=n&receiveUpdates=n&flag=7&phone=222222'+ add2 +'0&agentOwner=0'
        updateLeadReturn = main(url, headers, method, data)

        #Delete
        url = url
        method = 'DELETE'
        deleteSearchReturn = main(url, headers, method, data)
        print deleteSearchReturn

#only json works
output = 'json'
key = 'Wb6IHM-GT71Htdd-7rvN-_'
#apiversion = '1.4.0'

#default domain and headers
#rootUrl = 'https://api.idxbroker.com'
rootUrl = 'https://api.idxsandbox.com'

versions = ['1.0.4', '1.1.1', '1.2.0', '1.2.1', '1.2.2', '1.2.0', '1.3.0', '1.4.0']
#versions = ['1.4.0']


for version in versions:
    headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":version, "outputtype":output}
    data = '';
    crudMethods(rootUrl, data, headers)
