---
layout: post
title: "Linux permissions for www-pub group"
date: 2012-11-11 20:50:00 +02:00
updated: 2014-01-17 11:45:02 +02:00
categories: [linux]
tags: ["/var/www", "apache", "chmod", "chown", "config", "group", "linux", "permissions", "umask", "www"]
excerpt: "Create a new group (www-pub) and add the users to that group: groupadd www-pub usermod -a -G www-pub usera ## must use -a to append to existing groups usermod -a -G www-pub user..."
original_url: "https://koodinpatkia.blogspot.com/2012/11/linux-permissions-for-www-pub-group.html"
migrated: true
lang: en
---

Create a new group (www-pub) and add the users to that group:

```text
groupadd www-pub

usermod -a -G www-pub usera ## must use -a to append to existing groups
usermod -a -G www-pub userb
groups usera ## display groups for user
```

Change the ownership of everything under /var/www to root:www-pub

```text
chown -R root:www-pub /var/www ## -R for recursive
```
Change the permissions of all the folders to 2775

```text
chmod 2775 /var/www ## 2=set group id, 7=rwx for owner (root), 7=rwx for group (www-pub), 5=rx for world (including apache www-data user)
```
Set group ID (SETGID) bit (2) causes the group (www-pub) to be copied to all new files/folders created in that folder. Other options are SETUID (4) to copy the user id, and STICKY (1) which I think lets only the owner delete files.

There's a -R recursive option, but that won't discriminate between files and folders, so you have to use find, like so:

```text
find /var/www -type d -exec chmod 2775 {} +
```
Change all the files to 0664

```text
find /var/www -type f -exec chmod 0664 {} +
```
Change the umask for your users to 0002

The umask controls the default file creation permissions, 0002 means files will have 664 and directories 775. Setting this (by editing the umask line at the bottom of /etc/profile in my case) means files created by one user will be writable by other users in the www-group without needing to chmod them.

Test all this by creating a file and directory and verifying the owner, group and permissions with ls -l.

Note: You'll need to logout/in for changes to your groups to take effect!

Note: Add the following line to /etc/pam.d/login to set the user specific
umask at login:

```text
session optional pam_umask.so umask=0022
```

