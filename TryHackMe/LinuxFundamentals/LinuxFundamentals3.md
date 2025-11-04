# Linux Fundamentals 3

## Description

Welcome to part three (and the finale) of the Linux Fundamentals module. So far, throughout the series, you have got hands-on with some fundamental concepts and used some important commands. This room is going to showcase some useful utilities and applications that you are likely to use day-to-day. You're also going to advance your Linux-fu skills by learning about automation, package management, and service/application logging. 

### Terminal Text Editors

This room introduces Vim and nano text editors .

Features of VIM :

* Customisable - you can modify the keyboard shortcuts to be of your choosing
* Syntax Highlighting - this is useful if you are writing or maintaining code, making it a popular choice for software developers
* VIM works on all terminals where nano may not be installed
* There are a lot of resources such as cheatsheets, tutorials, and the sorts available to you use.

### General/Useful Utilities

This room introduces the file transfer techniques and tricks in linux.

* Downloading Files (Wget)
* Transferring Files From Your Host - SCP (SSH)
* Serving Files From Your Host - WEB

### Processes 101

Processes are the programs that are running on your machine. They are managed by the kernel, where each process will have an ID associated with it, also known as its PID. The PID increments for the order In which the process starts. I.e. the 60th process will have a PID of 60.

#### Viewing Processes

We can use the friendly ps command to provide a list of the running processes as our user's session and some additional information such as its status code, the session that is running it, how much usage time of the CPU it is using, and the name of the actual program or command that is being executed:

#### Managing Processes

You can send signals that terminate processes; there are a variety of types of signals that correlate to exactly how "cleanly" the process is dealt with by the kernel. To kill a command, we can use the appropriately named kill command and the associated PID that we wish to kill. i.e., to kill PID 1337, we'd use kill 1337.

Below are some of the signals that we can send to a process when it is killed:

* SIGTERM - Kill the process, but allow it to do some cleanup tasks beforehand
* SIGKILL - Kill the process - doesn't do any cleanup after the fact
* SIGSTOP - Stop/suspend a process

#### How do Processes Start?

Let's start off by talking about namespaces. The Operating System (OS) uses namespaces to ultimately split up the resources available on the computer to (such as CPU, RAM and priority) processes. Think of it as splitting your computer up into slices -- similar to a cake. Processes within that slice will have access to a certain amount of computing power, however, it will be a small portion of what is actually available to every process overall.

Namespaces are great for security as it is a way of isolating processes from another -- only those that are in the same namespace will be able to see each other.

We previously talked about how PID works, and this is where it comes into play. The process with an ID of 0 is a process that is started when the system boots. This process is the system's init on Ubuntu, such as systemd, which is used to provide a way of managing a user's processes and sits in between the operating system and the user. 

For example, once a system boots and it initialises, systemd is one of the first processes that are started. Any program or piece of software that we want to start will start as what's known as a child process of systemd. This means that it is controlled by systemd, but will run as its own process (although sharing the resources from systemd) to make it easier for us to identify and the likes.

#### Getting Processes/Services to Start on Boot

Some applications can be started on the boot of the system that we own. For example, web servers, database servers or file transfer servers. This software is often critical and is often told to start during the boot-up of the system by administrators.

In this example, we're going to be telling the apache web server to be starting apache manually and then telling the system to launch apache2 on boot.

Enter the use of systemctl -- this command allows us to interact with the systemd process/daemon. Continuing on with our example, systemctl is an easy to use command that takes the following formatting: systemctl [option] [service]

For example, to tell apache to start up, we'll use systemctl start apache2. Seems simple enough, right? Same with if we wanted to stop apache, we'd just replace the [option] with stop (instead of start like we provided)

We can do four options with systemctl:

* Start
* Stop
* Enable
* Disable



#### Questions and answers:

If we were to launch a process where the previous ID was "300", what would the ID of this new process be?

* 301

If we wanted to cleanly kill a process, what signal would we send it?

* SIGTERM 


Locate the process that is running on the deployed instance (10.201.65.124). What flag is given?

* THM{PROCESSES}

What command would we use to stop the service "myservice"?

* systemctl stop myservice


What command would we use to start the same service on the boot-up of the system?

* systemctl enable myservice

What command would we use to bring a previously backgrounded process back to the foreground?

* fg

#### Maintaining Your System: Automation

Users may want to schedule a certain action or task to take place after the system has booted. Take, for example, running commands, backing up files, or launching your favourite programs on, such as Spotify or Google Chrome.

We're going to be talking about the cron process, but more specifically, how we can interact with it via the use of crontabs . Crontab is one of the processes that is started during boot, which is responsible for facilitating and managing cron jobs.


Value		Description

MIN			What minute to execute at

HOUR		What hour to execute at

DOM			What day of the month to execute at

MON			What month of the year to execute at

DOW			What day of the week to execute at

CMD			The actual command that will be executed.


## Maintaining Your System: Package Management

### Introducing Packages & Software Repos

When developers wish to submit software to the community, they will submit it to an  "apt" repository. If approved, their programs and tools will be released into the wild. Two of the most redeeming features of Linux shine to light here: User accessibility and the merit of open source tools.

When using the ls command on a Ubuntu 20.04 Linux machine, these files serve as the gateway/registry. 

### Managing Your Repositories (Adding and Removing)

Normally we use the apt command to install software onto our Ubuntu system. The apt command is a part of the package management software also named apt. Apt contains a whole suite of tools that allows us to manage the packages and sources of our software, and to install or remove software at the same time.

One method of adding repositories is to use the add-apt-repository command we illustrated above, but we're going to walk through adding and removing a repository manually. Whilst you can install software through the use of package installers such as dpkg, the benefits of apt means that whenever we update our system -- the repository that contains the pieces of software that we add also gets checked for updates. 

In this example, we're going to add the text editor Sublime Text to our Ubuntu machine as a repository as it is not a part of the default Ubuntu repositories. When adding software, the integrity of what we download is guaranteed by the use of what is called GPG (Gnu Privacy Guard) keys. These keys are essentially a safety check from the developers saying, "here's our software". If the keys do not match up to what your system trusts and what the developers used, then the software will not be downloaded

## Maintaining Your System: Logs

This Task is all about to the log file structure and the observation of the log files.

