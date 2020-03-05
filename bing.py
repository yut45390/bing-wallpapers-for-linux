import requests
import os
import sys
import json
import subprocess

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
const="&n=1"
#extension
extn=".jpg"
# Size.
size="1920x1200"


reqImg=bing + api + format + day + market + const

r = requests.get(reqImg)
if r.status_code != 200:
    print("request status code is %d" % r.status_code)
    sys.exit(1)

res=r.content.decode("utf-8")
data=json.loads(res)
pathbase=os.path.join(os.environ.get("HOME"),"Public","Bing")
os.makedirs(pathbase,exist_ok=True)
img=data['images'][-1]
imageUrl=bing+img['url']
urlbase=img['urlbase']
print(bing+urlbase+"_"+size+extn)
key="id="
id_index = urlbase.find(key) + len(key)
imageName=os.path.join(pathbase,urlbase[id_index:]+'.jpg')
r = requests.get(imageUrl)
if r.status_code != 200:
    print("request status code is %d fetching image" % r.status_code)
    sys.exit(1)
f = open(imageName,"wb")
f.write(r.content)
f.close()
assert os.environ.get('XDG_CURRENT_DESKTOP') == 'GNOME'

completed=subprocess.run(['gsettings','set',
                          'org.gnome.desktop.background',
                          'picture-uri',
                          'file://' + imageName])
assert completed.returncode == 0
completed=subprocess.run(['gsettings','set',
                          'org.gnome.desktop.background',
                          'picture-options', 'zoom'])
assert completed.returncode == 0

