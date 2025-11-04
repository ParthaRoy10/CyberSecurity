# Linux Fundamentals 2

## Objectives

* Unlocking the potential of your first few commands by introducing you to using flags and arguments
* Advancing your knowledge of the filesystem to perform some more useful commands such as copying and moving files
* Discovering how access to files and folders is managed and how we can determine our access.
* Running your first few scripts and executables!

## Accessing Your Linux Machine Using SSH (Deploy)

In this room some basic Ideas Like how to connect via `ssh` is described .

Connect to the target system using `ssh`.

## Introduction to Flags and Switches

This room introduces the `flags` , `switches` and the `man(ual)` page . For seraral operations.

## Filesystem Interaction Continued

This room teaches about

* create files and folders
* move files and folders
* delete files and folders

## Permissions 101

This room is about basic file permission and the switching of users using `su` command.

## Common Directories

Describes the purpose of the common directories.

### /etc:

This root directory is one of the most important root directories on your system. The etc folder (short for etcetera) is a commonplace location to store system files that are used by your operating system. 

For example, the sudoers file highlighted in the screenshot below contains a list of the users & groups that have permission to run sudo or a set of commands as the root user.

Also highlighted below are the "passwd" and "shadow" files. These two files are special for Linux as they show how your system stores the passwords for each user in encrypted formatting called sha512.

### /var

The "/var" directory, with "var" being short for variable data,  is one of the main root folders found on a Linux install. This folder stores data that is frequently accessed or written by services or applications running on the system. For example, log files from running services and applications are written here (/var/log), or other data that is not necessarily associated with a specific user (i.e., databases and the like).

### /root

Unlike the /home directory, the /root folder is actually the home for the "root" system user. There isn't anything more to this folder other than just understanding that this is the home directory for the "root" user. But, it is worth a mention as the logical presumption is that this user would have their data in a directory such as "/home/root" by default

### /tmp

This is a unique root directory found on a Linux install. Short for "temporary", the /tmp directory is volatile and is used to store data that is only needed to be accessed once or twice. Similar to the memory on your computer, once the computer is restarted, the contents of this folder are cleared out.

What's useful for us in pentesting is that any user can write to this folder by default. Meaning once we have access to a machine, it serves as a good place to store things like our enumeration scripts.

