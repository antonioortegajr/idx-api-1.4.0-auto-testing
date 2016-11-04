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
    firstName = addOn + 'Bau'
    lastName = addOn + 'kim'
    email = addOn + 'kim.bau.bau.kim@gmail.com'
    data = {'firstName' : firstName, 'lastName' : lastName, 'email' : email}

    #Read
    method ='GET'
    main(url, headers, method, data)

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
        #now that we have a lead ID check create and update
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

        #before we delete the lead, lets check other endpoints that use a lead ID
        #check notes
        url = rootUrl + componant + '/note/' + createdLead
        method ='PUT'
        newNoteID = ''
        data = {'note' : 'test note'}
        newNoteReturn = main(url, headers, method, data)

        #check for an error
        if (newNoteReturn == 'ERROR'):
            print 'There was an ERROR. Check the errors.txt file'
        else:
            #now that we have a lead ID check create and update
            newNoteID = json.loads(newNoteReturn)
            createdNote = str(newNoteID['newID'])
            print createdNote

            #Update
            method = 'POST'
            url = url + '/' + createdNote
            newNoteName = 'new note'
            data = {'note' : newNoteName}
            updateNoteReturn = main(url, headers, method, data)
            print updateNoteReturn

            #Delete
            url = url
            method = 'DELETE'
            deleteNoteReturn = main(url, headers, method, data)
            print deleteNoteReturn



        #Delete
        url = rootUrl + componant + '/lead/' + createdLead
        method = 'DELETE'
        url = url
        deleteLeadReturn = main(url, headers, method, data)
        print deleteLeadReturn
