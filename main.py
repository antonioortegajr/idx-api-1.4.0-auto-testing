from leads.test import leadMethods
from mls.test import mlsMethods
from clients.test import clientsMethods
from partners.test import partnersMethods

key = 'NDd@2a7om0nIoZdFKqjXxX'
apiversion = '1.4.0'
output = 'json'
data = '';

#default domain and headers
rootUrl = 'https://api.idxbroker.com'
headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":apiversion, "outputtype":output}

#test Leads methods
#leadMethods(rootUrl, data, headers)

#test MLS methods
#mlsMethods(rootUrl, data, headers)

#test MLS Clientsw
clientsMethods(rootUrl, data, headers)

#test Partners methods
#parnter key
#key = 'YLYsuwps-9kG0PyicpGsQZ'
#partnersMethods(rootUrl, data, headers)
