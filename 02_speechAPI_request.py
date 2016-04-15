#! /usr/bin/env python
# coding: utf-8

import os
import sys
import json
import requests
import com.sigmaxyz.ml.speech.ms.speech_api as speech_api
import com.sigmaxyz.common.html_template as template

clientId = "14c6e142-5175-4fec-b168-d9c9948d4fcc" 
clientSecret = "1cd81cba858147798dc63b993d88e727" 
api = speech_api.speech_api(clientId, clientSecret)

text = "This is a demo to call microsoft text to speach service in python. hogehoge!"
content = api.text_to_speech(text, "en-US", True)
retext = api.speech_to_text(content, "en-US", 8000, "ulm")
'''
text = "roumaji de nyuuryoku suru to deru no kana. hoge hoge !"
content = api.text_to_speech(text, "ja-JP", True)
retext = api.speech_to_text(content, "ja-JP", 8000, "ulm")
'''

title = "Speech API sample"
template = template.html_template()
template.writeHtml(title, retext)




