import requests
import os
import sys
import json

bing="http://www.bing.com"
# API end point.
api="/HPImageArchive.aspx?"

# Response Format (json|xml).
format="&format=js"

# For day (0=current; 1=yesterday... so on).
day="&idx=0"

# Market for image.
market="&mkt=en-GB"

# API Constant (fetch how many).
const="&n=3"

# Image extension.
extn=".jpg"

# Size.
size="1920x1200"

path=os.path.join(os.environ.get("HOME"),"Pictures","Bing")

reqImg=bing + api + format + day + market + const
print(reqImg)
r = requests.get(reqImg)
if r.status_code != 200:
    print("request status code is %d" % r.status_code)
    sys.exit(1)

res=r.content.decode("utf-8")
data=json.loads(res)
for img in data['images']:
    print(bing+img['url'])
