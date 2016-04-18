#! /usr/bin/env python

import requests, json, urllib, ast

class identification_profile:
    
    def __init__(self, client_secret):
        self.client_secret = client_secret
        
    def create_profile(self, lang):
        
        url = "https://api.projectoxford.ai/spid/v1.0/identificationProfiles"
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = json.dumps({
            "locale": lang
            })

        res = requests.post(url, data=params, headers=headers)

        if res.ok:
            id = ast.literal_eval(res.text)
            return id['identificationProfileId']
        else:
            res.raise_for_status()

    def delete_profile(self, id):

        url = "https://api.projectoxford.ai/spid/v1.0/identificationProfiles/%s" % id
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = urllib.urlencode({
            })

        res = requests.delete(url, data=params, headers=headers)

        if res.ok:
            return res.ok
        else:
            res.raise_for_status()

    def get_all_profiles(self):

        url = "https://api.projectoxford.ai/spid/v1.0/identificationProfiles"
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = urllib.urlencode({
            })

        res = requests.get(url, data=params, headers=headers)

        if res.ok:
            result = []
            list = ast.literal_eval(res.text)
            for i in list:
                dict = ast.literal_eval(str(i))
                result.append(dict)
            return result
        else:
            res.raise_for_status()

    def get_profile(self, id):

        url = "https://api.projectoxford.ai/spid/v1.0/identificationProfiles/%s" % id
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = urllib.urlencode({
            })

        res = requests.get(url, data=params, headers=headers)

        if res.ok:
            result = ast.literal_eval(res.text)
            return result
        else:
            res.raise_for_status()

    def create_enrollment(self, id, content):

        url = "https://api.projectoxford.ai/spid/v1.0/identificationProfiles/%s/enroll" % id
        headers = {
            'Content-Type': 'multipart/form-data',
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = urllib.urlencode({
            })

        res = requests.post(url, data=content, headers=headers)

        if res.ok:
            result = res.text
            return result
        else:
            res.raise_for_status()

    def reset_enrollments(self, id):

        url = "https://api.projectoxford.ai/spid/v1.0/identificationProfiles/%s/reset" % id
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret,
            }
        params = urllib.urlencode({
            })

        res = requests.post(url, data=params, headers=headers)

        if res.ok:
            result = res.text
            return result
        else:
            res.raise_for_status()

class speaker_recognition:
    
    def __init__(self, client_secret):
        self.client_secret = client_secret
        
    def get_operation_status(self, id):
        
        url = "https://api.projectoxford.ai/spid/v1.0/operations/%s" % id
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = urllib.urlencode({
            })

        res = requests.get(url, data=params, headers=headers)

        if res.ok:
            result = ast.literal_eval(res.text)
            return result
        else:
            res.raise_for_status()

'''
    def identification(self, id):
    
        url = "https://api.projectoxford.ai/spid/v1.0/identify?identificationProfileIds=%s" % id
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.client_secret,
            }
        params = urllib.urlencode({
            })

        res = requests.post(url, data=params, headers=headers)

        if res.ok:
            result = res.text
            return result
        else:
            res.raise_for_status()

    def verification(self, id):
    
        url = "https://api.projectoxford.ai/spid/v1.0/verify?verificationProfileId=%s" % id
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.client_secret,
            }
        params = urllib.urlencode({
            })

        res = requests.post(url, data=params, headers=headers)

        if res.ok:
            result = res.text
            return result
        else:
            res.raise_for_status()
'''
class verification_phrase:

    def __init__(self, client_secret):
        self.client_secret = client_secret
        
    def list_all_supported_verification_phrases(self, lang):
        
        url = "https://api.projectoxford.ai/spid/v1.0/verificationPhrases?locale=%s" % lang
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = urllib.urlencode({
            })

        res = requests.get(url, data=params, headers=headers)

        if res.ok:
            result = []
            list = ast.literal_eval(res.text)
            for i in list:
                dict = ast.literal_eval(str(i))
                result.append(dict)
            return result
        else:
            res.raise_for_status()
           
class verification_profile:
    
    def __init__(self, client_secret):
        self.client_secret = client_secret
        
    def create_profile(self, lang):
        
        url = "https://api.projectoxford.ai/spid/v1.0/verificationProfiles"
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = json.dumps({
            "locale": lang
            })

        res = requests.post(url, data=params, headers=headers)

        if res.ok:
            id = ast.literal_eval(res.text)
            return id['verificationProfileId']
        else:
            res.raise_for_status()

    def delete_profile(self, id):

        url = "https://api.projectoxford.ai/spid/v1.0/verificationProfiles/%s" % id
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret
            }
        params = urllib.urlencode({
            })

        res = requests.delete(url, data=params, headers=headers)

        if res.ok:
            return res.ok
        else:
            res.raise_for_status()

    def get_all_profiles(self):

        url = "https://api.projectoxford.ai/spid/v1.0/verificationProfiles"
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret,
            }
        params = urllib.urlencode({
            })

        res = requests.get(url, data=params, headers=headers)

        if res.ok:
            result = []
            list = ast.literal_eval(res.text)
            for i in list:
                dict = ast.literal_eval(str(i))
                result.append(dict)
            return result
        else:
            res.raise_for_status()

    def get_profile(self, id):

        url = "https://api.projectoxford.ai/spid/v1.0/verificationProfiles/%s" % id
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret,
            }
        params = urllib.urlencode({
            })

        res = requests.get(url, data=params, headers=headers)

        if res.ok:
            result = ast.literal_eval(res.text)
            return result
        else:
            res.raise_for_status()

    def create_enrollment(self, id, content):

        url = "https://api.projectoxford.ai/spid/v1.0/verificationProfiles/%s/enroll" % id
        headers = {
            'Content-Type': 'multipart/form-data',
            'Ocp-Apim-Subscription-Key': self.client_secret,
            }

        res = requests.post(url, data=content, headers=headers)

        if res.ok:
            result = res.text
            return result
        else:
            res.raise_for_status()

    def reset_enrollments(self, id):

        url = "https://api.projectoxford.ai/spid/v1.0/verificationProfiles/%s/reset" % id
        headers = {
            'Ocp-Apim-Subscription-Key': self.client_secret,
            }
        params = urllib.urlencode({
            })

        res = requests.post(url, data=params, headers=headers)

        if res.ok:
            result = res.text
            return result
        else:
            res.raise_for_status()
