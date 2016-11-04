from leads.test import leadMethods
from mls.test import mlsMethods

key = 'NDd@2a7om0nIoZdFKqjXxX'
partnerKey = '';
apiversion = '1.4.0'
output = 'json'
data = '';

#default domain and headers
rootUrl = 'https://api.idxbroker.com'
headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":apiversion, "outputtype":output}

#test Leads methods
#leadMethods(rootUrl, data, headers)

#test MLS methods
mlsMethods(rootUrl, data, headers)
