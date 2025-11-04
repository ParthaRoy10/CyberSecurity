import requests as req
import re


username="natas3"
password='3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH'

url="http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"

response=req.get(url,auth=(username,password))

print(re.findall("natas4:(.*)",response.text)[0])

