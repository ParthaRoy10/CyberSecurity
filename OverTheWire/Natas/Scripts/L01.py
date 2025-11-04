import requests as req
import re


username="natas0"
password='natas0'

url="http://natas0.natas.labs.overthewire.org"

response=req.get(url,auth=(username,password))


print (re.findall("<!--The password for natas1 is (.*) -->",response.text)[0])