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
Append ' init=/bin/sh' to the end of the linux line.
You should then have a '# ' prompt.
The root filesystem will be mounted read-only.
Remount the file system in read write mode by entering: mount -o remount,rw /
(This is not needed?) Unlock the 'root' account: passwd -u root
Change the 'root' account password: passwd root