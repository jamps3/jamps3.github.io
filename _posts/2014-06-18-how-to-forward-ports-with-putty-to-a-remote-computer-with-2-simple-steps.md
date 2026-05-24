---
layout: post
title: "How to forward ports with Putty to a remote computer with 2 simple steps"
date: 2014-06-18 18:04:00 +03:00
updated: 2014-06-23 15:53:32 +03:00
categories: [linux]
tags: ["port forwarding", "ports", "putty", "ssh"]
excerpt: "In putty configuration: Connection → SSH → Tunnels: Here I used a random port 58808: 1) Input \"127.0.0.2:58808\" to Source port, you can also use \"localhost:58808\" or \"127.0.0.1:..."
original_url: "https://koodinpatkia.blogspot.com/2014/06/how-to-forward-ports-with-putty-to.html"
migrated: true
lang: en
---

In putty configuration: Connection → SSH → Tunnels:

Here I used a random port 58808:

<a href="{{ '/assets/blog/images/puttyconfig2.png' | relative_url }}" imageanchor="1"><img border="0" src="{{ '/assets/blog/images/puttyconfig2.png' | relative_url }}" height="397" width="400" /></a>

1) Input "127.0.0.2:58808" to Source port, you can also use "localhost:58808" or "127.0.0.1:58808", depending on compatibility and preference.

2) input "localhost:58808" to Destination, 

3) Check "Local" and "Auto", then click "Add".

<a href="{{ '/assets/blog/images/puttyconfig1.png' | relative_url }}" imageanchor="1"><img border="0" src="{{ '/assets/blog/images/puttyconfig1.png' | relative_url }}" height="398" width="400" /></a>

And you're done!

Now you can connect to your localhost(127.0.0.2) using your defined port and it will forward it to your remote computer.

You can also forward to different and multiple ports, if desired.

