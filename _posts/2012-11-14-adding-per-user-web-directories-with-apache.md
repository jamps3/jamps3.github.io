---
layout: post
title: "Adding per-user web directories with Apache"
date: 2012-11-14 21:32:00 +02:00
updated: 2014-01-17 11:44:24 +02:00
categories: [linux]
tags: ["apache", "config", "user", "www"]
excerpt: "Open Apache2 config file: sudo nano /etc/apache2/apache2.conf Add these lines in the end, change *your_username* to yours: # UserDir # UserDir public_html UserDir disabled UserD..."
original_url: "https://koodinpatkia.blogspot.com/2012/11/adding-per-user-web-directories-with.html"
---

Open Apache2 config file:
<code class="prettyprint">
sudo nano /etc/apache2/apache2.conf
</code>
Add these lines in the end, change *your_username* to yours:
<code class="prettyprint">
# UserDir #
UserDir public_html
UserDir disabled
UserDir enabled *your_username*
Options Indexes FollowSymLinks -MultiViews AllowOverride None Order allow,deny Allow from all
</code>
Make symbolic links for mod_userdir to enable it:
<code class="prettyprint">
cd /etc/apache2/mods-available/
sudo ln -s ../mods-available/userdir.conf
sudo ln -s ../mods-available/userdir.load
</code>
Or enable the module without editing any files:
<code class="prettyprint">
a2enmod userdir
</code>
Remember to restart Apache:
<code class="prettyprint">
service apache2 restart
</code>
