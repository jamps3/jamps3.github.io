---
layout: post
title: "Adding per-user web directories with Apache"
date: 2012-11-14 21:32:00 +02:00
updated: 2014-01-17 11:44:24 +02:00
categories: [linux]
tags: ["apache", "config", "user", "www"]
excerpt: "Open Apache2 config file: sudo nano /etc/apache2/apache2.conf Add these lines in the end, change *your_username* to yours: # UserDir # UserDir public_html UserDir disabled UserD..."
original_url: "https://koodinpatkia.blogspot.com/2012/11/adding-per-user-web-directories-with.html"
migrated: true
lang: en
---

Open Apache2 config file:

```text
sudo nano /etc/apache2/apache2.conf
```
Add these lines in the end, change *your_username* to yours:

```text
# UserDir #
UserDir public_html
UserDir disabled
UserDir enabled *your_username*
Options Indexes FollowSymLinks -MultiViews AllowOverride None Order allow,deny Allow from all
```
Make symbolic links for mod_userdir to enable it:

```text
cd /etc/apache2/mods-available/
sudo ln -s ../mods-available/userdir.conf
sudo ln -s ../mods-available/userdir.load
```
Or enable the module without editing any files:

```text
a2enmod userdir
```
Remember to restart Apache:

```text
service apache2 restart
```

