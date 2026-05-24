---
layout: post
title: "Speed up computer with Ramdrive"
date: 2014-07-07 13:06:00 +03:00
updated: 2014-07-16 12:42:02 +03:00
categories: [linux]
tags: ["blogger-import", "linux", "web"]
excerpt: "1) Make a small Ramdisk of 64-512MB size(use Dataram Ramdisk Lite: http://memory.dataram.com/products-and-services/software/ramdisk) 2) Create a small swap file to your Ramdisk,..."
original_url: "https://koodinpatkia.blogspot.com/2014/07/speed-up-computer-with-ramdrive.html"
migrated: true
lang: en
---

1) Make a small Ramdisk of 64-512MB size(use Dataram Ramdisk Lite: <a href="http://memory.dataram.com/products-and-services/software/ramdisk" target="_blank">http://memory.dataram.com/products-and-services/software/ramdisk)</a>

2) Create a small swap file to your Ramdisk, 32-128MB is fine.

3) Move your firefox cache to the Ramdisk, limiting it's size to available space (30MB is fine if you don't have much RAM to spend), check here: [Set firefox cache location]({{ '/blog/2014/04/13/move-set-firefox-cache-location/' | relative_url }})

4) Restart Firefox and check if it creates the temp directory you specified(and monitor that it doesn't grow out of hand!).

5) Done!

I have found that making just a tiny Ramdisk where you put a little bit of swap seems to make computer faster. If you need more swap, create a few gigs swap somewhere on your HDD/SSD.

