from leads.test import leadMethods
from mls.test import mlsMethods
from clients.test import clientsMethods
from partners.test import partnersMethods

#only json works
output = 'json'
key = 'NDd@2a7om0nIoZdFKqjXxX'
#parnter key
partnerKey = 'YLYsuwps-9kG0PyicpGsQZ'
apiversion = '1.4.0'

#default domain and headers
rootUrl = 'https://api.idxbroker.com'
headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":apiversion, "outputtype":output}
data = '';

#test Leads methods and clear data variable after
leadMethods(rootUrl, data, headers)
data = '';

#test MLS methods
mlsMethods(rootUrl, data, headers)
data = '';

#test MLS Client
clientsMethods(rootUrl, data, headers)
data = '';

#test Partners methods
headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":partnerKey, "apiversion":apiversion, "outputtype":output}
partnersMethods(rootUrl, data, headers)
