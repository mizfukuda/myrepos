#! /usr/bin/env python

import os
import sys
import json
import requests
import com.sigmaxyz.ml.vision.ms.face_api as face_api

api = face_api.face_api()

result,message = api.request("http://www.sigmaxyz.com/wp-content/themes/sigmaxyz/_contents/corporateinfo/_img/greeting_bod_img_01.jpg",
                            "true",
                            "true")

if result == requests.codes.ok:
    print(message)
else:  # err
    print('stauts_code: {} (reason: {})'.format(result, message))
    sys.exit(1)
