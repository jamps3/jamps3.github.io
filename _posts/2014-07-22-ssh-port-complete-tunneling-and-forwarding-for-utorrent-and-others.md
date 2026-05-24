---
layout: post
title: "SSH Port complete tunneling and forwarding for uTorrent and others"
date: 2014-07-22 20:36:00 +03:00
updated: 2014-08-06 11:50:48 +03:00
categories: [linux]
tags: ["advanced", "port forwarding", "ports", "proxy", "socks5", "ssh"]
excerpt: "Someone(Dchard) on the Internet has found a possible solution(typos corrected): 1. Set up an SSH connection in Putty with the tunneling settings below: - Local ports accepts con..."
original_url: "https://koodinpatkia.blogspot.com/2014/07/ssh-port-complete-tunneling-and.html"
migrated: true
lang: en
---

Someone(Dchard) on the Internet has found a possible solution(typos corrected):

1. Set up an SSH connection in Putty with the tunneling settings below:

- Local ports accepts connections from other hosts [tick]

- Remote ports do the same [tick]

- Set up a dynamic port forward with source port 8080 (this will force the ssh server to act as a socks server)

- Set up a remote port forward with source port 50000, and Destination  127.0.0.1:50000 (this will forward the server's 50000 port to the local 50000 port. This could be changed if port 50000 is not open on the server).

Note that the forwarded ports (remote port forward) on the server side  are bound to the loopback interface by default, so you must first check your SSH server's config, and set "GatewayPorts yes" in it's config file (sshd.conf). By default GatewayPorts is set to no!

2. Connect via SSH (note that in default, only the root user can forward ports)

3. Set up uTorrent with the following settings:

- Port used for incoming connections: 50000

- Proxy server: Socks5

- Proxy address: 127.0.0.1

- Proxy port: 8080

- Select resolve hostnames through proxy

- Do not select Authentication, and Use proxy for peer to peer

Go to advanced settings an set bt.allow_same_ip to "true"

Restart uTorrent.

What we can achieve with this:

Now from behind a firewall and/or a proxy with even no direct internet connection we managed to get uTorrent working in active mode.

With the above settings the tracker announces are working, the peer list got downloaded, the uTorrent port checker says that the port forwards are OK, and the download starts and there are several incoming connections (flag I set) among the clients, and the uploads are also working fine.

