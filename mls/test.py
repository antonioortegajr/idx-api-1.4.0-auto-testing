from apiCall import main
import json

def mlsMethods(rootUrl, data, headers):
    componant = '/mls'

    #test listcomponents
    endPoint = '/listcomponents'
    url = rootUrl + componant + endPoint
    method = 'GET'
    listcomponents = main(url, headers, method, data)

    #test listmethods
    endPoint = '/listmethods'
    url = rootUrl + componant + endPoint
    listmethods = main(url, headers, method, data)

    #test approvedmls
    endPoint = '/approvedmls'
    url = rootUrl + componant + endPoint
    approvedmls = main(url, headers, method, data)

    #check for an error
    if (approvedmls == 'ERROR'):
        print 'There was an ERROR. Check the errors.text file'
    else:
        mlsReturn = json.loads(approvedmls)
        mlsReturn = mlsReturn[0]
        mlsID = str(mlsReturn['id'])
        print mlsID

    #test approvedmls
    endPoint = '/approvedmls'
    url = rootUrl + componant + endPoint
    approvedmls = main(url, headers, method, data)

    #test cities
    endPoint = '/cities/' + mlsID
    url = rootUrl + componant + endPoint
    cities  = main(url, headers, method, data)

    #test counties
    endPoint = '/counties/' + mlsID
    url = rootUrl + componant + endPoint
    counties = main(url, headers, method, data)

    #test zipcodes
    endPoint = '/zipcodes/' + mlsID
    url = rootUrl + componant + endPoint
    zipcodes = main(url, headers, method, data)

    #test prices
    endPoint = '/prices/' + mlsID
    url = rootUrl + componant + endPoint
    prices = main(url, headers, method, data)

    #test propertytypes
    endPoint = '/propertytypes/' + mlsID
    url = rootUrl + componant + endPoint
    propertytypes = main(url, headers, method, data)

    #test propertycount
    endPoint = '/propertycount/' + mlsID +'?countType=city&countSpecifier=37536'
    url = rootUrl + componant + endPoint
    propertycount = main(url, headers, method, data)

    #test age
    endPoint = '/age/' + mlsID
    url = rootUrl + componant + endPoint
    age = main(url, headers, method, data)

    #test searchfields
    endPoint = '/searchfields/' + mlsID
    url = rootUrl + componant + endPoint
    searchfields = main(url, headers, method, data)
