#! /usr/bin/env python

import urllib
import json
import requests

class speech_api:
    
    def __init__(self, client_id, client_secret):
        url = "https://oxford-speech.cloudapp.net//token/issueToken"

        headers = {
            "Content-type": "application/x-www-form-urlencoded"
        }

        params = urllib.urlencode(
            {"grant_type": "client_credentials",
             "client_id": client_id,
             "client_secret": client_secret,
             "scope": "https://speech.platform.bing.com"}
        )

        res = requests.post(url, data=params, headers=headers)

        if res.ok:
            _body = res.json()
            self.token = _body["access_token"]
            #return _body["access_token"]
        else:
            res.raise_for_status()

        
    def text_to_speech(self, text, lang, female):
        template = """
            <speak version='1.0' xml:lang='{0}'>
                <voice xml:lang='{0}' xml:gender='{1}' name='{2}'>
                    {3}
                </voice>
            </speak>
            """

        url = "https://speech.platform.bing.com/synthesize"
        headers = {
            "Content-type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
            "Authorization": "Bearer " + self.token,
            "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
            "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
            "User-Agent": "OXFORD_TEST"
        }
        name = "Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)"
        data = template.format(lang, "Female" if female else "Male", name, text)

        res = requests.post(url, data=data, headers=headers)

        if res.ok:
            return res.content
        else:
            raise res.raise_for_status()

            
    def speech_to_text(self, binary, lang, samplerate, scenarios):
        data = binary
        params = {
            "version": "3.0",
            "appID": "D4D52672-91D7-4C74-8AD8-42B1D98141A5",
            "instanceid": "1ECFAE91408841A480F00935DC390960",
            "requestid": "b2c95ede-97eb-4c88-81e4-80f32d6aee54",
            "format": "json",
            "locale": lang,
            "device.os": "Windows10",
            "scenarios": scenarios,
        }

        url = "https://speech.platform.bing.com/recognize/query?" + urllib.urlencode(params)
        headers = {"Content-type": "audio/wav; samplerate={0}".format(samplerate),
                   "Authorization": "Bearer " + self.token,
                   "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
                   "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
                   "User-Agent": "OXFORD_TEST"}

        res = requests.post(url, data=data, headers=headers)

        if res.ok:
            result = res.json()["results"][0]
            return result["lexical"]
        else:
            raise res.raise_for_status()
