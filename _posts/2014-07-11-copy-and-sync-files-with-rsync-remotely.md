---
layout: post
title: "Copy and sync files with rsync remotely"
date: 2014-07-11 16:08:00 +03:00
updated: 2014-07-11 16:09:48 +03:00
categories: [notes]
tags: ["copy", "files", "remote", "rsync", "sync"]
excerpt: "Copying files using rsync from remote server to local machine Using rsync is as simple as remembering 2 or 3 parameters. rsync -a [SOURCE] [DESTINATION] -a uses archive mode so..."
original_url: "https://koodinpatkia.blogspot.com/2014/07/copy-and-sync-files-with-rsync-remotely.html"
migrated: true
lang: en
---

<h4>
Copying files using rsync from remote server to local machine</h4>
Using rsync is as simple as remembering 2 or 3 parameters. 

rsync -a [SOURCE] [DESTINATION]

-a uses archive mode so the file permissions and parameters are kept. It is not required.

I usually use verbose and compression, so it looks like this:

rsync -avz [SOURCE] [DESTINATION]

for remote connections, [SOURCE] and [DESTINATION] can both be in the form:

user@host:/path/ 

If you want to include **hidden **files, try:

rsync -a ~/.[^.]* /path/to/backup

Here is part of the synopsis from the rsync man page:

       Local:  rsync [OPTION...] SRC... [DEST]

       Access via remote shell:

         Pull: rsync [OPTION...] [USER@]HOST:SRC... [DEST]

         Push: rsync [OPTION...] SRC... [USER@]HOST:DEST

       Usages with just one SRC arg and no DEST arg will list the source files

       instead of copying.

You can schedule it to run in 15 minute intervals by typing "crontab -e" and adding the following line to the end:

*/15 * * * * rsync [SRC] [DEST] 1&gt;/dev/null 2&gt;/dev/null

