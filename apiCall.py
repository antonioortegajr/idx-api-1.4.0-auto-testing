import httplib
import urlparse
import urllib
import requests
import json
import sys

#this is a call to base API calls off of.
def main(url, headers, method, data):

  params = data
  response = '';

  #retrun a true or false for valid or non valid json
  def is_json(response):
      try:
          json_object = json.loads(response)
          print '... valid json'
      except ValueError, e:
          print '... INVALD JSON'
          errorLog.write('Error found with: ' + url + ' http code: ' + httpStatusCode + ' JSON INVALID ' + '\n')

  #check to see if this is not a Read only call, oh yeah no swith in python
  if (method != 'GET'):
      if (method == 'PUT'):
          r = requests.put(url, data = params, headers=headers, verify=False)
      if (method == 'POST'):
          r = requests.post(url, data = params, headers=headers, verify=False)
      if (method == 'DELETE'):
          r = requests.delete(url, data = params, headers=headers, verify=False)
  else:
      r = requests.get(url, data = params, headers=headers, verify=False)

  #print the endpoint to be tested
  print '... START Testing ' + method + ' for ' + url + ' ...'
  response = r.text

  # print the http status code returned. Expecting 200
  httpStatusCode = str(r.status_code)
  print "status: " + httpStatusCode

  #Just exit if the API call limit is reached
  if(r.status_code == 412):
      print '... ERROR 412 stopping test'
      errorLog.write('Error found with : ' + url + ' http code: ' + httpStatusCode + ' Stopping test OVER API CALL LIMITS ' + '\n')
      sys.exit()

  #open a file to log any errors
  errorLog = open('errors.txt','a')
  responseLenth = len(response)

  #check that 200 and 204 have the correct string legnth
  if (r.status_code < 300):
      #no switch in python. Meh.
      if(r.status_code == 204 and responseLenth > 0):
          print '... ERROR 204 http response non empty return body. Should return 200...'
          errorLog.write('Error found with: ' + method + ' for ' + url + ' http code: ' + httpStatusCode + ' Return body does not match status code' + response + '\n')
      if (r.status_code == 200 and responseLenth == 0):
          print '... ERROR 200 http response with an empty return body. Should return 204...'
          errorLog.write('Error found with: ' + method + ' for ' + url + ' http code: ' + httpStatusCode + ' Return body does not match status code' + response + '\n')
      elif (r.status_code == 200):
          is_json(response)
          return response

  else:
      #log the errors in a text file
      errorLog.write('Error found with: ' + method + ' for ' + url + ' http code: ' + httpStatusCode + response + '\n')
      response = 'ERROR'
