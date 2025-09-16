# Lab: Username enumeration via different responses

 This lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

* [Candidate usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)

* [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

# Solution:

Access the lab.

Start BurpSuite .

Intercept the request using BurpSuite. 

Take the request to `repeater` and send the request tho show the response .

We can see the response `Invalid username` . That indicates that it first checks for the `username` if the Username does not matches then it returns the response `Invalid username`.
This leads us to brute-force us to find the right user names that are registerd with .

To enamurate the usernames obtain the username list from the lab description.

Send the request to `intruder` then Seelct the `username` section, as payload select `simple list` and attack type `sniper attack`. In seettings add select `Invalid username` in `grep extract`. Start the attack.

In one of our response we can see we have the response `Incorrect password` . That indicates the correct username . 

Now set the `username` parameter as the username we found. And to get the password for the username repeat the same process with `password` parameter .

One we got the username and the password login in the lab ...   We have successfully solved lab1 of Authentication .