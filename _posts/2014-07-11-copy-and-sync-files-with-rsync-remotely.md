---
layout: post
title: "Copy and sync files with rsync remotely"
date: 2014-07-11 16:08:00 +03:00
updated: 2014-07-11 16:09:48 +03:00
categories: [notes]
tags: ["copy", "files", "remote", "rsync", "sync"]
excerpt: "Copying files using rsync from remote server to local machine Using rsync is as simple as remembering 2 or 3 parameters. rsync -a [SOURCE] [DESTINATION] -a uses archive mode so..."
original_url: "https://koodinpatkia.blogspot.com/2014/07/copy-and-sync-files-with-rsync-remotely.html"
---

<h4>
Copying files using rsync from remote server to local machine</h4>
Using rsync is as simple as remembering 2 or 3 parameters. <br />
<br />
rsync -a [SOURCE] [DESTINATION]<br />
<br />
-a uses archive mode so the file permissions and parameters are kept. It is not required.<br />
I usually use verbose and compression, so it looks like this:<br />
rsync -avz [SOURCE] [DESTINATION]<br />
<br />
for remote connections, [SOURCE] and [DESTINATION] can both be in the form:<br />
user@host:/path/ <br />
<br />
If you want to include <b>hidden </b>files, try:<br />
rsync -a ~/.[^.]* /path/to/backup<br />
<br />
Here is part of the synopsis from the rsync man page:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Local:&nbsp; rsync [OPTION...] SRC... [DEST]<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Access via remote shell:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pull: rsync [OPTION...] [USER@]HOST:SRC... [DEST]<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Push: rsync [OPTION...] SRC... [USER@]HOST:DEST<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Usages with just one SRC arg and no DEST arg will list the source files<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; instead of copying.<br />
<br />
You can schedule it to run in 15 minute intervals by typing "crontab -e" and adding the following line to the end:<br />
*/15 * * * * rsync [SRC] [DEST] 1&gt;/dev/null 2&gt;/dev/null
