---
layout: post
title: "How to set Firefox to use Ramdisk as a cache to speed it up"
date: 2012-12-11 22:43:00 +02:00
updated: 2014-09-22 15:25:32 +03:00
categories: [notes]
tags: ["browser", "computer", "performance", "ram", "ramdisk", "speed"]
excerpt: "1) Download Dataram Ramdisk directly from this link http://adf.ly/Fr1ff 2) Install & configure Ramdisk. 3) in Firefox, type about:config 4) Make new String \"browser.cache.disk.p..."
original_url: "https://koodinpatkia.blogspot.com/2012/12/set-firefox-to-use-ramdisk-as-cache-to.html"
migrated: true
lang: en
---

1) Download Dataram Ramdisk directly from this link <a href="http://adf.ly/Fr1ff">http://adf.ly/Fr1ff</a>

2) Install &amp; configure Ramdisk.

3) in Firefox, type **about:config**

4) Make new String **"browser.cache.disk.parent_directory"**

5) Set value **"K:\fftemp\"**, replacing K with your Ramdisk drive letter.

Done!

Note: Firefox might not respect the size limit for it's cache directory! Missing pictures in Firefox etc. will ensue if the cache drive gets full.

