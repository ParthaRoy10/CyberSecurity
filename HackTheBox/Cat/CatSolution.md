# Cat Walkthrough

## Description:

Easy leaks

## Solution:

Download the [Cat.zip](files/cat.zip) and unzip the file . The password for the zip file `hackthebox`.

After unzipping the file I have run `file` command on it to learn about the file type.

```
file cat.ab              
cat.ab: Android Backup, version 5, Compressed, Not-Encrypted
```

The file is an android backup type file.

To read the file we first need to convert the file into `tar` archaive then unzipping it will return us the files.

To convert the files into `tar` files I have used `(printf '\x1f\x8b\x08\x00\x00\x00\x00\x00'; tail -c +25 cat.ab) | tar xvfz -` . The command returns us two files `apps` and `shared`.

In `shared` we have couple of images.

After opening the images one by one We have found the flag .

The hint for the box was the cat images.

![[Image](files/Answer.png)](files/Answer.png)

flag :	HTB{ThisBackupIsUnprotected}
