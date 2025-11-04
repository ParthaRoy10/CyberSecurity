# Lab: Username enumeration via subtly different responses

 This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

* Candidate usernames
* Candidate passwords

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

# Solution :

Int this lab we got the response as `Invalid username or password.` .

But the lab points outs there is a small change(subtly) in different responses.

Use the techniques used in [lab1.md] .

This time carefully watch that enamurating `usernames` the response gets a small change of `.` .

