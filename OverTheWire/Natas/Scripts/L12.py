import requests as req
import re

from urllib.parse import unquote

"""
The response initially tells us that the cookies are 'xor' encrypted.

Let's check the cookies.

The cookies are endcoded in url encoding First we decrypt it to url .

The cookie is encoded in base64 . Let's decode the cookie.

Xor encryption:     cipher text= plaintext+ key

Similerly for finding the key : key= cipher text + plaintext

We have 
palintext = {"showpassword":"no","bgcolor":"#ffffff"}
ciphertext = f$3'7  uUG*8MIf5+;fmMF"1	"1M

key= eDWo

plaintext={"showpassword":"yes","bgcolor":"#ffffff"}
ciphertext=HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5
Now craft the cookie similer way .

I have used Cyberchef for encryption and decryption of the cookie.

"""

username="natas11"
password='UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk'

url="http://%s.natas.labs.overthewire.org/" % username

cookie={
    "data":"HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5"
}

s=req.Session()
response=s.post(url,auth=(username,password),cookies=cookie)
cookie=response.cookies.get_dict()



print(re.findall("The password for natas12 is (.*)<br>",response.text)[0])



