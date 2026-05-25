# Bandit 

## Level 0

### Hint 

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

### Solution

Connect with the ssh shell 

## Level 0

### Hint 

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

### Solution

Read the readme file 

Password : `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

## Level 1

### Hint 

The password for the next level is stored in a file called - located in the home directory

### Solution

The file name `-` is actually a special character . We can read the file with the fully qualified name with the path. 

Command to read the file : `cat ./-`

Password : 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

## Level 2

### Hint 

The password for the next level is stored in a file called --spaces in this filename-- located in the home directory

### Solution 

We can solve the level same concept with the previous but this time we have to enclose the name within the quotations 

Command : `cat ./"--spaces in this filename--"`

Password : `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

## Level 3

### Hint 

The password for the next level is stored in a hidden file in the inhere directory.

### Solution

Use `ls -la` To revel the hidden file under the folder . And read the file .

Command : `cat ./...Hiding-From-You`

Password : `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`


## Level 4

### Hint 

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

### Solution

Let's first find the Files that are human-readable means contains ascii or utf.

`for i in {0..10}; do file ./-file0${i}; done`

Now read the human readable file .

Password : `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

## Level 5

### Hint

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

    human-readable
    1033 bytes in size
    not executable


### Solution 

This Time we have a list of files . The required password file can be within any of it .

Let's find the file with the given criteria ..

`find . -size 1033c 2>/dev/null ! -executable`

We have only one file in the output, so we can read the file for the password .

Password : `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`


## Level 6

### Hint 

The password for the next level is stored somewhere on the server and has all of the following properties:

    owned by user bandit7
    owned by group bandit6
    33 bytes in size


### Solution 

Find the File 

`find / -size 33c -user bandit7 -group bandit6 -type f 2>/dev/null`

Password : `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

## Level 7

### Hint 

The password for the next level is stored in the file data.txt next to the word millionth

### Solution

Use grep to find the line containig the word millionth 

Password : `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

## Level 8

### Hint 

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

### Solution 

Use Sort , and uniq together to find the string that occured once .

`cat data.txt | sort | uniq -c`

Password : `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

## Level 9 

### Hint 

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

### Solution

Use string command to get the human-redable strings 

Paasword : `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

## Level 10 

### Hint 

The password for the next level is stored in the file data.txt, which contains base64 encoded data

### Solution

Decode the data .

Password : `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

## Level 11

### Hint 

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.

### Solution 

Just ROT13 cipher

`cat data.txt | tr [n-za-mN-ZA-M] [a-zA-Z]`

Password : `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

## Level 12

### Hint 

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

### Solution

There are multiple encoding in placed .. Unzip all. But first create the actual file ` cat data.txt | xxd -r`

Password : `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

## Level 13

### Hint 

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.

### Solution 

Here We have the private key. Store the key locally and use it for ssh login.

## Level 14 

### Hint 

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.nc localhost 

### Solution

After logging in with the private ssh key first read the password of bandit14.

Now submit the password in port 30000 to get the password for bandit15

Password :
	Bandit14 : `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`
	Bandit15 : `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo`
	
## Level 15

### Hint 

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

### Solution 

`openssl s_client -connect localhost:30001` 

Use openssl client .

Password : `kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx`

## Level 16

### Hint

 The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.


### Solution 

First find the open ports 

```
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown
```

To find the ports talk in ssl use this script 

```
#!/bin/bash

nums=(31046 31518 31691 31790 31960)
input_str="kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx"

for i in "${nums[@]}"  
do
        if echo "$input_str" | openssl s_client -connect localhost:$i -quiet 2>/dev/null; then
                echo "Success port no $i"
        else
                echo "Failed port no $i"
        fi
done


```
Got the private key of level17 .

Use the private key for login

## Level 17

### Hint 

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see 'Byebye!' when trying to log into bandit18, this is related to the next level, bandit19

### Solution

USe diff command 

```
bandit17@bandit:~$ diff passwords.new passwords.old 
42c42
< x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
---
> KxOU4IzbXM8j8HeAWPAXTd1eC77mp1qV
```

## Level 18

### Hint

The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

### Solution 

The main problem here is when we login in bandit 18 the bash prompt closes immidiately. 

To get a interactive shell 

`ssh bandit18@bandit.labs.overthewire.org -p 2220 "sh" `

This is basic shell . 

Now read the file containing the password .

Password : `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

## Level 19

### Hint 

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

### Solution 

Read the file using the binary  

Command : `./bandit20-do cat /etc/bandit_pass/bandit20`
Password : `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

## Level 20

### Hint 

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

### Solution

Use nc to build a Connection using binary Then pass the current pass in the nc terminal to get the password.

Terminal 1 : ```
nc -lnvp 1234                                                                                 
Listening on 0.0.0.0 1234                                                                                        
Connection received on 127.0.0.1 48488                                                                           
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
```

Terminal 2 : ```
./suconnect 1234 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
```

## Level 21

### Hint 

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed

### Solution

Check the Cron file located in `/etc/cron.d/cronjob_bandit22` And get the file from the file where the password 

## Level 22

### Hint 

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

### Solution

Similer as Previous . Analyze the script . Don't forget the md5.

Password : `0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`


## Level 23

### Hint 

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

### Solution

Check the script first :

```
#!/bin/bash 		-> 

shopt -s nullglob	-> changes how Bash handles file-matching patterns (wildcards) when no matching files are found. By default, if you type a wildcard like *.txt and no such files exist, Bash passes the literal string *.txt to your command; enabling nullglob makes Bash pass nothing at all instead.

myname=$(whoami)

cd /var/spool/"$myname"/foo || exit 
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." ] && [ "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" "./$i")"
        if [ "${owner}" = "bandit23" ] && [ -f "$i" ]; then
            timeout -s 9 60 "./$i"
        fi
        rm -rf "./$i"
    fi
```

The scri[t suggests that the script run once every script present in ` /var/spool/$myname/foo` directory where the user name is `bandit23` , then delets the script .

To get the password write a script

```
#!/bin/bash

cat  /etc/bandit_pass/bandit24 > /tmp/tmp.xYBptdbBe8/pass.txt
```

Change the file permissions and (For pass.txt also) And place it to `/var/spool/bandit24/foo/" directory and wait for some time .

Password : `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

## Level 24

## Hint



A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time

### Solution

Create the bruteforcer for the given connection

```
#!/bin/bash

password="gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"

for i in {0000..9999}; do
        echo "$password $i"
done | nc localhost 30002
```

Password	:	`iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`

## Level 25

### Hint 

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

    NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.

### Solution

Exploit the functionality of more buffer to get the interactive shell.

First reduce the size of the terminal (First download the ssh key then try to connect with the target from base system not from the ssh terminal of banddit25) Then open vi editor and get the shell.

## Level 26

### Hint 

Good job getting a shell! Now hurry and grab the password for bandit27!

### Solution

There is one binary with SUID . Greab the password

```
./bandit27-do cat /etc/bandit_pass/bandit27
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```

## Level 27

### Hint

There is a git repository at ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.


### Solution

Download the git file and extract check the commoit history of the file .

Password : 'Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN'

## Level 28

### Hint 

There is a git repository at ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.


### Solution 

As previous check the commit history.

Password : `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`

## Level 29

### Hint 

There is a git repository at ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Solution 

Search in different branches . It is there .

Password : `qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`

## Level 30

### Hint 

There is a git repository at ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

### Solution

Check the tags this time.

Password : `fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`

## Level 31

### Hint 

There is a git repository at ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine

### Solution

```
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

```

Create a new key.txt and try pushin the remote host. Remember the gitignore file . Wo overcome add the file manually.

Password : `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`

## Level 32

### Hint 

After all this git stuff, it’s time for another escape. Good luck!

### Solution

To get the actual shell path try the Environment variables 

```
>> $SHELL		--> This is overwritten
WELCOME TO THE UPPERCASE SHELL
>> $0			--> This works fine
$ whoami
bandit33
```
Password : 	`tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0`

## Level 33

Completed ...................................







