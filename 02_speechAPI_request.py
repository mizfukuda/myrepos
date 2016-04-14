#! /usr/bin/env python

import os
import sys
import json
import requests
import com.sigmaxyz.ml.speech.ms.speech_api as speech_api

clientId = "14c6e142-5175-4fec-b168-d9c9948d4fcc" 
clientSecret = "1cd81cba858147798dc63b993d88e727" 
text = "This is a demo to call microsoft text to speach service in python."

api = speech_api.speech_api(clientId, clientSecret)

content = api.text_to_speech(text, "en-US", True)

retext = api.speech_to_text(content, "en-US", 8000, "ulm")

print("ReText is ... " + retext)



