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
        
api = speaker_recognition_api.verification_profile(clientSecret)

id = api.create_profile("en-US")
output = "プロファイルIDを取得：" + str(id) + "</br>"

list = api.get_all_profiles()
output += "プロファイルリストを取得</br>"
for dict in list:
    output += str(dict['verificationProfileId']) + "</br>"

profile = api.get_profile(id)
output += "プロファイルIDを取得：" + str(profile) + "</br>"

api.delete_profile(id)


title = "SpeakerRecognition API sample - verification_profile"
template = template.html_template()
template.writeHtml(title, output)

