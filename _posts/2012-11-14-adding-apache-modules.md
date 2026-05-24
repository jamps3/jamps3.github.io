---
layout: post
title: "Adding Apache modules"
date: 2012-11-14 21:44:00 +02:00
updated: 2014-01-17 11:41:36 +02:00
categories: [linux]
tags: ["a2enmod", "apache", "drupal", "modules", "service", "www"]
excerpt: "The following may work to enable modules without editing any files: a2enmod modulename For example, this module is used for Clean URLs(Good for Drupal): a2enmod rewrite Remember..."
original_url: "https://koodinpatkia.blogspot.com/2012/11/adding-apache-modules.html"
---

The following may work to enable modules without editing any files:
<code class="prettyprint">
a2enmod modulename
</code>
For example, this module is used for Clean URLs(Good for Drupal):
<code class="prettyprint">
a2enmod rewrite
</code>
Remember to restart Apache:
<code class="prettyprint">
service apache2 restart
</code>
