#! /usr/bin/env python

import urllib
import json
import requests,ast

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

        if res.ok:
            result = []
            list = ast.literal_eval(res.text)
            for i in list:
                dict = ast.literal_eval(str(i))
                result.append(dict)
            return result
        else:
            raise res.raise_for_status()

