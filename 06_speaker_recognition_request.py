#! /usr/bin/env python
# coding: utf-8

import os
import sys
import json
import requests,ast
import com.sigmaxyz.ml.speech.ms.speaker_recognition_api as speaker_recognition_api
import com.sigmaxyz.ml.speech.ms.speech_api as speech_api
import com.sigmaxyz.common.html_template as template

clientSecret = "1a42dc0db0624a2a989c838d79935da3"
        
api0 = speaker_recognition_api.identification_profile(clientSecret)
id = api0.create_profile("en-US")


api1 = speaker_recognition_api.speaker_recognition(clientSecret)
dict = api1.get_operation_status(id)
print(dict)

'''
title = "SpeakerRecognition API sample - verification_profile"
template = template.html_template()
template.writeHtml(title, output)
'''