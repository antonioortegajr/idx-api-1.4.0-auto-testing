from leads.test import leadMethods
from mls.test import mlsMethods
from clients.test import clientsMethods
from partners.test import partnersMethods

#from crud.test import crudMethods
from notesCrud.test import notesCrudMethods
from propertyCrud.test import propertyCrudMethods

#only json works
output = 'json'
key = 'yourKey'
#parnter key
partnerKey = 'yourKey'
apiversion = '1.4.0'

#default domain and headers
#rootUrl = 'https://api.idxbroker.com'
rootUrl = 'https://api.idxsandbox.com'

headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":key, "apiversion":apiversion, "outputtype":output}
data = ''

#test CRUD Methods
#crudMethods(rootUrl, data, headers)

#test notes Crud Methods
#notesCrudMethods(rootUrl, data, headers)

#test notes Crud Methods
propertyCrudMethods(rootUrl, data, headers)

#test Leads methods and clear data variable after
#leadMethods(rootUrl, data, headers)
data = ''

#test MLS methods
#mlsMethods(rootUrl, data, headers)
data = ''

#test MLS Client
#clientsMethods(rootUrl, data, headers)
data = ''

#test Partners methods
#headers = {"Content-Type":"application/x-www-form-urlencoded", "accesskey":partnerKey, "apiversion":apiversion, "outputtype":output}
#partnersMethods(rootUrl, data, headers)
