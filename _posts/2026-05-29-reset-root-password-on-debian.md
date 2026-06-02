---
layout: post
title: "Reset root password on Debian"
date: 2026-05-29 02:22:35 +03:00
updated: 2026-05-29 02:22:35 +03:00
categories: ["Linux"]
tags: ["linux", "debian", "passwords"]
excerpt: "How to reset 'root' password on local Debian"
lang: "en"
migrated: false
---

If the boot loader isn't locked, after GRUB shows:
Hit 'e' to edit the boot entry.
Append this to the end of the linux line:
```Text
 init=/bin/sh
```
You should then have a '# ' prompt.
The root filesystem will be mounted read-only.
Remount the file system in read write mode by entering:
```Text
mount -o remount,rw /
```
Change the 'root' account password:
```Text
passwd root
```