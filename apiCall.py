import httplib
import urlparse
import urllib
import requests

#this is a sample call to base API calls off of.
def main(url, headers, method, data):

  params = urllib.urlencode(data)

  #check to see if this is not a Read only call, oh yeah no swith in python
  if (method != 'GET'):
      if (method == 'PUT'):
          print params
          r = requests.put(url, data = params, headers=headers)

      if (method == 'POST'):
          r = requests.post(url, data = params, headers=headers)

      if (method == 'DELETE'):
          r = requests.delete(url, data = params, headers=headers)
  else:
      r = requests.get(url, data = params, headers=headers)

  #print the endpoint to be tested
  print '... START Testing ' + method + ' for ' + url + ' ...'
  response = r.text

  # print the http status code returned. Expecting 200
  httpStatusCode = str(r.status_code)
  print "status: " + httpStatusCode

  #log the error
  errorLog = open('errors.txt','a')
  responseLenth = len(httpStatusCode)

  #check that 200 and 204 have the correct string legnth
  if (r.status_code < 300):

      #no switch in python. Meh.
      if(r.status_code == 204 and responseLenth > 0):
          print '... ERROR 204 http response non empty return body. Should return 200...'
          errorLog.write('Error found with: ' + url + ' http code: ' + httpStatusCode + ' Return body does not match status code' + response + '\n')
      if (r.status_code == 200 and responseLenth == 0):
          print '... ERROR 200 http response with an empty return body. Should return 204...'
          errorLog.write('Error found with: ' + url + ' http code: ' + httpStatusCode + ' Return body does not match status code' + response + '\n')
  else:
      #log the errors in a text file
      errorLog.write('Error found with: ' + url + ' method: ' + method + ' http code: ' + httpStatusCode + response + '\n')
      response = 'ERROR'

  print r.headers
  return response
  print '... END Testing '+method+' for '+url+' ...'
