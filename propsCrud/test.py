from apiCall import main
import json

def propertyCrudMethods(rootUrl, data, headers):
    componant = '/leads'

    #test lead methods
    endPoint = '/lead'
    url = rootUrl + componant + endPoint
    #Create Lead
    method ='PUT'
    newLeadID = ''

    # numbers each time this function is called
    add = data + data
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

        #create a notes
        method ='PUT'
        endPoint = '/note/'
        url = rootUrl + componant + endPoint + createdLead
        data = 'propertyName=Test+Property&property%5BidxID%5D=a001&property%5BlistingID%5D=345678'
        newPropertyReturn = main(url, headers, method, data)

        #check for an error
        if (newPropertyReturn == 'ERROR'):
            print 'There was an ERROR. Check the errors.text file'

        else:
            #now that we have a lead ID check create and update
            newPropertyeID = json.loads(newPropertyReturn)
            createdProperty = str(newPropertyID['newID'])
            print createdProperty

            #Read note
            method ='GET'
            url = url
            main(url, headers, method, data)

            #Update note
            method = 'POST'
            url = url + '/' + createdProperty
            data = 'propertyName=Test+Property123&property%5BidxID%5D=a001&property%5BlistingID%5D=1234567890'
            updateNoteReturn = main(url, headers, method, data)

            #Delete
            url = url
            method = 'DELETE'
            deletePropertyReturn = main(url, headers, method, data)
            print deleteNPropertyReturn

            method = 'DELETE'
            endPoint = '/lead/'
            url = rootUrl + componant + endPoint + createdLead
            deleteLeadReturn = main(url, headers, method, data)






#only json works
output = 'json'
key = 'Wb6IHM-GT71Htdd-7rvN-_'
#apiversion = '1.4.0'

#default domain and headers
#rootUrl = 'https://api.idxbroker.com'
rootUrl = 'https://api.idxsandbox.com'

versions = ['1.4.0', '1.3.0', '1.2.2', '1.2.1', '1.2.0', '1.1.1', '1.0.4']
#versions = ['1.4.0']


for version in versions:
    headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":version, "outputtype":output}
    data = '123';
    propertyCrudMethods(rootUrl, data, headers)
