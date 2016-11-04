from apiCall import main

def partnersMethods(rootUrl, data, headers):
    componant = '/partners'

    #test listcomponents
    endPoint = '/listcomponents'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test listmethods
    endPoint = '/listmethods'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)
    
    #test clients
    endPoint = '/clients'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test propertytypes
    endPoint = '/propertytypes/'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedleads
    endPoint = '/aggregatedleads'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedsearches
    endPoint = '/aggregatedsearches'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedproperties
    endPoint = '/aggregatedproperties'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test clients
    endPoint = '/aggregatedleadtraffic'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedfeatured
    endPoint = '/aggregatedfeatured'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedsupplemental
    endPoint = '/aggregatedsupplemental'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedsoldpending
    endPoint = '/aggregatedsoldpending'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedlistingstatus
    endPoint = '/aggregatedlistingstatus'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test aggregatedagents
    endPoint = '/aggregatedagents'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)
