import requests as req
import re


username="natas1"
password='0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq'

url="http://natas1.natas.labs.overthewire.org"

response=req.get(url,auth=(username,password))


print (re.findall("<!--The password for natas2 is (.*) -->",response.text)[0])