#! /usr/bin/env python

import urllib
import json
import requests

class face_api:
    
    def __init__(self):
        self.url = "https://api.projectoxford.ai/face/v1.0/detect?returnFaceId=%s&returnFaceLandmarks=%s"
        self.headers = {'Content-Type' : 'application/json',
                        'Ocp-Apim-Subscription-Key' : '3504ddc8ec0a45df9b675c1f177269d5'}

    def request(self,imagePath,returnFaceId,returnFaceLandmarks):
        res = requests.post(self.url % (returnFaceId,returnFaceLandmarks),
                            data=json.dumps({'url' : imagePath}),
                            headers=self.headers
                            )
        '''
        if res.status_code == requests.codes.ok:
            self.status_code = res.status_code
            self.ans = res.text
        else:  # err
            self.status_code = res.status_code
            self.ans = self.reason
        return self.status_code,self.ans
        '''
        if res.ok:
            return res.text
        else:
            raise res.raise_for_status()

