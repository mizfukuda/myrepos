#! /usr/bin/env python
# coding: utf-8

import os
import sys
import json
import requests
import com.sigmaxyz.ml.vision.ms.face_api as face_api
import com.sigmaxyz.common.html_template as template

    
api = face_api.face_api()
result = api.request("http://www.sigmaxyz.com/wp-content/themes/sigmaxyz/_contents/corporateinfo/_img/greeting_bod_img_01.jpg",
                            "true",
                            "true")
                            
title = "Face API sample"
template = template.html_template()
template.writeHtml(title, result)
