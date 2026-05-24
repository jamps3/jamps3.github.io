---
layout: post
title: "Disable SSH Reverse DNS Lookup"
date: 2012-11-11 20:45:00 +02:00
updated: 2014-01-17 11:45:37 +02:00
categories: [linux]
tags: ["config", "debian", "linux", "ssh"]
excerpt: "If not disabled, SSH server will try to do a slow reverse lookup of the IP address of the client causing for an unnecessary delay during authentication. I often have this case a..."
original_url: "https://koodinpatkia.blogspot.com/2012/11/disable-ssh-reverse-dns-lookup.html"
---

If not disabled, SSH server will try to do a slow reverse lookup of the IP address of the client causing for an unnecessary delay during authentication. I often have this case after installing Linux.<br />
<br />
To disable it, in the file /etc/ssh/sshd_config add the line below:<br />
<code class="prettyprint">
UseDNS no
</code>
