#! /usr/bin/env python

### 
#Copyright (c) Microsoft Corporation 
#All rights reserved.  
#MIT License 
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ""Software""), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
#THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
### 
#import http.client, 
#from urllib3.parse.urlencode import urllib3
import requests, json, sys
 
#VoiceSynthesisRequest

#Note: Sign up at http://www.projectoxford.ai to get a subscription key.   
#Search for Speech APIs from Azure Marketplace. 
#Use the subscription key as Client secret below. 
clientId = "14c6e142-5175-4fec-b168-d9c9948d4fcc" 
clientSecret = "1cd81cba858147798dc63b993d88e727" 
ttsHost = "https://speech.platform.bing.com" 

url0 = "https://oxford-speech.cloudapp.net/token/issueToken"
params0 = {'grant_type': 'client_credentials', 'client_id': clientId, 'client_secret': clientSecret, 'scope': ttsHost}
headers0 = {"Content-type": "application/x-www-form-urlencoded"} 

print ("The body data: %s" %(params0)) 

#params0 = urllib3.parse.urlencode({'grant_type': 'client_credentials', 'client_id': clientId, 'client_secret': clientSecret, 'scope': ttsHost}) 
#AccessTokenHost = "oxford-speech.cloudapp.net" 
#path = "/token/issueToken" 
# Connect to server to get the Oxford Access Token 
#conn = http.client.HTTPSConnection(AccessTokenHost) 
#conn.request("POST", path, params, headers) 
#response = conn.getresponse() 
#conn.close() 

response0 = requests.post(
    url0,
    data=json.dumps(params0),
    headers=headers0
    )
print(response0.status_code, response0.reason) 

data = response0.text
#accesstoken = data.decode("UTF-8") 
accesstoken = data
print ("Oxford Access Token: " + accesstoken) 

#decode the object from json 
ddata=json.loads(accesstoken) 
access_token = ddata['access_token'] 

url = "https://speech.platform.bing.com/synthesize"
body = "<speak version='1.0' xml:lang='en-us'><voice xml:lang='en-us' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>This is a demo to call microsoft text to speach service in python.</voice></speak>" 
headers = {"Content-type": "application/ssml+xml",  
    	   "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",  
	       "Authorization": "Bearer " + access_token,  
	       "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",  
	       "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",  
	       "User-Agent": "TTSForPython"} 

#Connect to server to synthesize the wave 
response = requests.post(
    url,
    data=json.dumps(body),
    headers=headers
    )

# output
if response.status_code == requests.codes.ok:
    print(response.text)
else:  # err
    print('stauts_code: {} (reason: {})'.format(response.status_code, response.reason))
    sys.exit(1)

'''
data = response.Text
#conn.close() 
print("The synthesized wave length: %d" %(len(data))) 
'''