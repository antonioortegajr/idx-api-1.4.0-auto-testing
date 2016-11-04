from apiCall import main
import json

#Lead componant testing

def leadMethods(rootUrl, data, headers):
    componant = '/leads'

    #test listcomponents
    endPoint = '/listcomponents'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test listmethods
    endPoint = '/listmethods'
    method = 'GET'
    url = rootUrl + componant + endPoint
    listmethods = main(url, headers, method, data)

    #test lead methods
    endPoint = '/lead'
    url = rootUrl + componant + endPoint
    addOn = 'lmnop'
    firstName = 'Bau'
    lastName = 'kim'
    email = 'kim.bau.bau.kim@gmail.com' + addOn
    data = {'firstName' : firstName, 'lastName' : lastName, 'email' : email}

    #Create
    method ='PUT'
    newLeadID = ''
    newLeadReturn = main(url, headers, method, data)
    #sample return {"newID":39}
    print newLeadReturn

    #check for an error
    if (newLeadReturn == 'ERROR'):
        print 'There was an ERROR. Check the errors.text file'

    else:
        newLeadID = json.loads(newLeadReturn)
        createdLead = str(newLeadID['newID'])
        print createdLead

        #Update
        method = 'POST'
        url = url + '/' + createdLead
        newLastName = lastName + 'testForPostUpdate'
        data = {'lastName' : newLastName}
        updateLeadReturn = main(url, headers, method, data)
        print updateLeadReturn

        #Delete
        method = 'DELETE'
        url = url
        deleteLeadReturn = main(url, headers, method, data)
        print deleteLeadReturn

    #Read
    method ='GET'
    main(url, headers, method, data)
