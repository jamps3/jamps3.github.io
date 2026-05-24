---
layout: post
title: "How to forward ports with Putty to a remote computer with 2 simple steps"
date: 2014-06-18 18:04:00 +03:00
updated: 2014-06-23 15:53:32 +03:00
categories: [linux]
tags: ["port forwarding", "ports", "putty", "ssh"]
excerpt: "In putty configuration: Connection → SSH → Tunnels: Here I used a random port 58808: 1) Input \"127.0.0.2:58808\" to Source port, you can also use \"localhost:58808\" or \"127.0.0.1:..."
original_url: "https://koodinpatkia.blogspot.com/2014/06/how-to-forward-ports-with-putty-to.html"
---

In putty configuration: Connection → SSH → Tunnels:<br />
<br />Here I used a random port 58808:<br />
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIQajuFQlhD0CI7yymI0i5CuLPF2ssDRZHtRdq9o46I2OwKdEEMw5hW5-tQX6QLiGUPGFEMerlS9bENSn0gtJF030KW-zfptXTv1esbLu52c1yO3NOFYzPFXsCHvI9GzwldKJ76qeGAnw/s1600/puttyconfig2.png" imageanchor="1"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIQajuFQlhD0CI7yymI0i5CuLPF2ssDRZHtRdq9o46I2OwKdEEMw5hW5-tQX6QLiGUPGFEMerlS9bENSn0gtJF030KW-zfptXTv1esbLu52c1yO3NOFYzPFXsCHvI9GzwldKJ76qeGAnw/s1600/puttyconfig2.png" height="397" width="400" /></a><br />
<br />
1) Input "127.0.0.2:58808" to Source port, you can also use "localhost:58808" or "127.0.0.1:58808", depending on compatibility and preference.<br />
2) input "localhost:58808" to Destination, <br />
3) Check "Local" and "Auto", then click "Add".<br />
<br />
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlxlIRUcclJn9pDM1P-piSVJ1i7sDgIum2NO-XufSLxQHmXclEFem_E-d5l3LmjROeXqffiB6eLbuWGkzHf-ikwAqsfpMt_LA4ip-jybYq-j-_jrnj1GpQ_owD4FcZZtl5aCGHNojkZ1o/s1600/puttyconfig1.png" imageanchor="1"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlxlIRUcclJn9pDM1P-piSVJ1i7sDgIum2NO-XufSLxQHmXclEFem_E-d5l3LmjROeXqffiB6eLbuWGkzHf-ikwAqsfpMt_LA4ip-jybYq-j-_jrnj1GpQ_owD4FcZZtl5aCGHNojkZ1o/s1600/puttyconfig1.png" height="398" width="400" /></a><br />
<br />
And you're done!<br />
<br />
Now you can connect to your localhost(127.0.0.2) using your defined port and it will forward it to your remote computer.<br />
You can also forward to different and multiple ports, if desired.
