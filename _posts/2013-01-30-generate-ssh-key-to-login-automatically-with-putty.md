---
layout: post
title: "Generate SSH key to login automatically with putty"
date: 2013-01-30 23:47:00 +02:00
updated: 2014-06-18 17:59:22 +03:00
categories: [linux]
tags: ["automatic", "key", "keyfile", "login", "putty", "remote login", "ssh"]
excerpt: "Use puttygen.exe to make a private key. Make .ssh/authorized_keys file and add text ” ssh-rsa ” with spaces, following the public key from the private key file on one line. Assi..."
original_url: "https://koodinpatkia.blogspot.com/2013/01/generate-ssh-key-to-login-automatically.html"
---

Use puttygen.exe to make a private key.<br />
Make .ssh/authorized_keys file and add text ” ssh-rsa ” with spaces,<br />
following the public key from the private key file on one line.<br />
Assign rw permissions only for the owner.
<code>$ chmod 600 ~/.ssh/authorized_keys.</code><br />
Configure putty to use the private key when connecting (Connection -&gt; SSH -&gt; Auth).<br />
<br />
More detailed instructions: <a href="http://www.tonido.com/blog/index.php/2009/02/20/ssh-without-password-using-putty/">http://www.tonido.com/blog/index.php/2009/02/20/ssh-without-password-using-putty/</a>
