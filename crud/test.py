from apiCall import main
import json

def crudMethods(rootUrl, data, headers):
    componant = '/leads'

    #test lead methods
    endPoint = '/lead'
    url = rootUrl + componant + endPoint
    add = "q"
    add = add + 'w'
    firstName = addOn + 'Bau'
    lastName = addOn + 'kim'
    email = addOn + 'kim.bau.bau.kim@gmail.com'
    email2 = addOn + 'kim.bau.bau2.kim@gmail.com'
    password = 'password'
    address ='123 fake'
    city = 'fake'
    stateProvince = 'OR'
    country = 'usa'
    zipCode = 'HTML' #HTML or Plain Text
    disabled = 'n' #y or n
    canLogin = 'y' #y or n
    receiveUpdates = 'y' #y or n
    flag = 'y' #y or n
    phone = '1234567890'
    agentOwner = '1'


    data = {'firstName' : firstName, 'lastName' : lastName, 'email' : email, 'email2': addOn, 'password': password, 'address': address, 'city': city, 'stateProvince': stateProvince, 'country': country, 'zipCode': zipCode, 'disabled': disabled, disabled, 'canLogin': canLogin, 'receiveUpdates': receiveUpdates, 'flag': flag, 'phone': phone, 'agentOwner': agentOwner}

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
        endPoint = '/lead'
        url = rootUrl + componant + endPoint
        add = "q222"
        add = add + 'w222'
        firstName = addOn + 'Bau'
        lastName = addOn + 'kim'
        email = addOn + 'kim.bau.bau.kim@gmail.com'
        email2 = addOn + 'kim.bau.bau2222.kim@gmail.com'
        password = 'changeme'
        address ='1234567 fake'
        city = 'fakesss'
        stateProvince = 'Ro'
        country = 'ussr'
        zipCode = 'Plain Text' #HTML or Plain Text
        disabled = 'y' #y or n
        canLogin = 'n' #y or n
        receiveUpdates = 'n' #y or n
        flag = 'n' #y or n
        phone = '0987654321'
        agentOwner = '1'


        data = {'firstName' : firstName, 'lastName' : lastName, 'email' : email, 'email2': addOn, 'password': password, 'address': address, 'city': city, 'stateProvince': stateProvince, 'country': country, 'zipCode': zipCode, 'disabled': disabled, disabled, 'canLogin': canLogin, 'receiveUpdates': receiveUpdates, 'flag': flag, 'phone': phone, 'agentOwner': agentOwner}

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

#versions = ['1.0.4', '1.1.1', '1.2.0', '1.2.1', '1.2.2', '1.2.0', '1.3.0', '1.4.0']
versions = ['1.4.0']


data = '';
for version in versions:
    headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":version, "outputtype":output}
    crudMethods(rootUrl, data, headers)
