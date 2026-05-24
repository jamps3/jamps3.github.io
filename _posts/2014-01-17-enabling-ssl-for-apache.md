---
layout: post
title: "Enabling ssl for Apache"
date: 2014-01-17 10:52:00 +02:00
updated: 2014-06-18 18:01:04 +03:00
categories: [linux]
tags: ["apache", "server", "ssl", "web"]
excerpt: "Website needs to be both enabled AND available. For this, you need to create a symbolic link into the sites-enabled folder and restart Apache : cd /etc/apache2/sites-enabled ln..."
original_url: "https://koodinpatkia.blogspot.com/2014/01/enabling-ssl-for-apache.html"
migrated: true
lang: en
---

Website needs to be both enabled AND available.

For this, you need to create a symbolic link into the sites-enabled folder and restart Apache:

```text
cd /etc/apache2/sites-enabled

ln -s ../sites-available/default-ssl default-ssl

/etc/init.d/apache2 reload
```

