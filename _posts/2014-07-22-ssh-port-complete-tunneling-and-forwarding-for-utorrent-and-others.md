---
layout: post
title: "SSH Port complete tunneling and forwarding for uTorrent and others"
date: 2014-07-22 20:36:00 +03:00
updated: 2014-08-06 11:50:48 +03:00
categories: [linux]
tags: ["advanced", "port forwarding", "ports", "proxy", "socks5", "ssh"]
excerpt: "Someone(Dchard) on the Internet has found a possible solution(typos corrected): 1. Set up an SSH connection in Putty with the tunneling settings below: - Local ports accepts con..."
original_url: "https://koodinpatkia.blogspot.com/2014/07/ssh-port-complete-tunneling-and.html"
---

Someone(Dchard) on the Internet has found a possible solution(typos corrected):<br />
<br />
1. Set up an SSH connection in Putty with the tunneling settings below:<br />
<br />
- Local ports accepts connections from other hosts [tick]<br />
- Remote ports do the same [tick]<br />
- Set up a dynamic port forward with source port 8080 (this will force the ssh server to act as a socks server)<br />
- Set up a remote port forward with source port 50000, and Destination  127.0.0.1:50000 (this will forward the server's 50000 port to the local 50000 port. This could be changed if port 50000 is not open on the server).<br />
<br />
Note that the forwarded ports (remote port forward) on the server side  are bound to the loopback interface by default, so you must first check your SSH server's config, and set "GatewayPorts yes" in it's config file (sshd.conf). By default GatewayPorts is set to no!<br />
<br />
2. Connect via SSH (note that in default, only the root user can forward ports)<br />
<br />
3. Set up uTorrent with the following settings:<br />
<br />
- Port used for incoming connections: 50000<br />
- Proxy server: Socks5<br />
- Proxy address: 127.0.0.1<br />
- Proxy port: 8080<br />
- Select resolve hostnames through proxy<br />
- Do not select Authentication, and Use proxy for peer to peer<br />
<br />
Go to advanced settings an set bt.allow_same_ip to "true"<br />
<br />
Restart uTorrent.<br />
<br />
What we can achieve with this:<br />
<br />
Now from behind a firewall and/or a proxy with even no direct internet connection we managed to get uTorrent working in active mode.<br />
<br />
With the above settings the tracker announces are working, the peer list got downloaded, the uTorrent port checker says that the port forwards are OK, and the download starts and there are several incoming connections (flag I set) among the clients, and the uploads are also working fine.<br />

