---
layout: post
title: "Rsync hidden files from home directory for backup purposes"
date: 2014-07-11 15:57:00 +03:00
updated: 2014-07-11 15:57:43 +03:00
categories: [notes]
tags: ["backup", "files", "hidden", "rsync"]
excerpt: "rsync -a ~/.[^.]* /path/to/backup you can also use: -v for verbose -z for compression"
original_url: "https://koodinpatkia.blogspot.com/2014/07/rsync-hidden-files-for-backup-purposes.html"
migrated: true
lang: en
---

rsync -a ~/.[^.]* /path/to/backup

you can also use:

-v for verbose

-z for compression

