#! /usr/bin/env python
# coding: utf-8

import os
import sys
import json
import requests,ast
import com.sigmaxyz.ml.speech.ms.speaker_recognition_api as speaker_recognition_api
import com.sigmaxyz.ml.speech.ms.speech_api as speech_api
import com.sigmaxyz.common.html_template as template

## this is making content for test create_enrollment
clientId0 = "14c6e142-5175-4fec-b168-d9c9948d4fcc" 
clientSecret0 = "1cd81cba858147798dc63b993d88e727" 
text = "This is a demo to call microsoft text to speach service in python. hogehoge!"
api0 = speech_api.speech_api(clientId0, clientSecret0)
content = api0.text_to_speech(text, "en-US", True)

## test create_enrollment
clientSecret = "1a42dc0db0624a2a989c838d79935da3"
        
api = speaker_recognition_api.identification_profile(clientSecret)
id = api.create_profile("en-US")

result_create = api.create_enrollment(id, content)
print(result_create)
result_reset = api.reset_enrollments(id)
print(result_reset)

