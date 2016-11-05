from apiCall import main
import json

def clientsMethods(rootUrl, data, headers):
    componant = '/clients'

    #test listcomponents
    endPoint = '/listcomponents'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test listmethods
    endPoint = '/listmethods'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listmethods = main(url, headers, method, data)

    #test agents
    endPoint = '/agents'
    url = rootUrl + componant + endPoint
    method = 'GET'
    agents = main(url, headers, method, data)

    #test offices
    endPoint = '/offices'
    url = rootUrl + componant + endPoint
    method = 'GET'
    offices = main(url, headers, method, data)

    #test systemlinks
    endPoint = '/systemlinks'
    url = rootUrl + componant + endPoint
    method = 'GET'
    systemlinks = main(url, headers, method, data)

    #test widgetsrc
    endPoint = '/widgetsrc'
    url = rootUrl + componant + endPoint
    method = 'GET'
    widgetsrc = main(url, headers, method, data)

    #test featured
    endPoint = '/featured'
    url = rootUrl + componant + endPoint
    method = 'GET'
    featured = main(url, headers, method, data)

    #test featured
    endPoint = '/soldpending'
    url = rootUrl + componant + endPoint
    method = 'GET'
    soldpending = main(url, headers, method, data)

    #test supplemental
    endPoint = '/supplemental'
    url = rootUrl + componant + endPoint
    method = 'GET'
    supplemental = main(url, headers, method, data)

    #test cities
    endPoint = '/cities'
    url = rootUrl + componant + endPoint
    method = 'GET'
    cities = main(url, headers, method, data)

    #test citieslistname
    endPoint = '/citieslistname'
    url = rootUrl + componant + endPoint
    method = 'GET'
    citieslistname = main(url, headers, method, data)

    #test counties
    endPoint = '/counties'
    url = rootUrl + componant + endPoint
    method = 'GET'
    counties = main(url, headers, method, data)

    #test zipcodes
    endPoint = '/zipcodes'
    url = rootUrl + componant + endPoint
    method = 'GET'
    zipcodes = main(url, headers, method, data)

    #test accounttype
    endPoint = '/accounttype'
    url = rootUrl + componant + endPoint
    method = 'GET'
    accounttype = main(url, headers, method, data)

    #test wrappercache
    endPoint = '/wrappercache'
    url = rootUrl + componant + endPoint
    method = 'DELETE'
    wrappercache = main(url, headers, method, data)

    #Create SavedSearch
    endPoint = '/savedlinks'
    url = rootUrl + componant + endPoint
    method ='PUT'
    newSearchID = ''
    data = 'linkName=Auto_testing&pageTitle=Auto_testing&linkTitle=Auto_testing&queryString%5BidxID%5D=a001&queryString%5Bhp%5D=200000'
    newSearchReturn = main(url, headers, method, data)
    #sample return {"newID":39}
    print newSearchReturn

    #check for an error
    if (newSearchReturn == 'ERROR'):
        print 'There was an ERROR. Check the errors.text file'

    else:
        #now that we have a Search ID check create and update
        newSearchID = json.loads(newSearchReturn)
        createdSearch = str(newSearchID['newID'])
        print createdSearch

        #Update
        method = 'POST'
        url = url + '/' + createdSearch
        newSearchName = 'new search'
        data = 'linkName=newTempSearchName'
        updateSearchReturn = main(url, headers, method, data)
        print updateSearchReturn

        #Delete
        url = url
        method = 'DELETE'
        deleteSearchReturn = main(url, headers, method, data)
        print deleteSearchReturn
