import requests as req
import re



username="natas8"
password='xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q'

url="http://%s.natas.labs.overthewire.org/" % username

data={
    "secret":"oubWYf2kBq",
    "submit":"submit"
}
s=req.Session()
response=s.post(url,auth=(username,password),data=data)

print(re.findall("Access granted. The password for natas9 is (.*)",response.text)[0])


