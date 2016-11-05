#Auto Testing IDX Broker API methods

NONE of this will be supported by IDX Broker in ANY way.

Please DO NOT contact IDX Broker support regarding this repo.

##Use

Add your API key to the key variable in main.py
You can always change the version, but this is not specifically supported
XML is not supported
Comment out any test you do not want to run in main.py

Test all the methods for:
* Correct response code of success 200 or 204
* Response code above 300 are logged as error
* Correct response length based on success code
* Valid json


Dependancies:
Install any you don't have with PIP
* json
* sys
* [requests](http://docs.python-requests.org/en/master/)
* [httplib](https://docs.python.org/2/library/httplib.html)
* [urlparse](https://docs.python.org/2/library/urlparse.html)
* [urllib](https://docs.python.org/2/library/urllib.html)

Required:
* valid IDX Broker API key
* valid IDX Broker Partner key
* use of only a001 for now
