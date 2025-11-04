import requests as req
import re

username="natas2"
password='TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI'

url="http://natas2.natas.labs.overthewire.org/files/users.txt"

response=req.get(url,auth=(username,password))


print(re.findall("natas3:(.*)",response.text)[0])