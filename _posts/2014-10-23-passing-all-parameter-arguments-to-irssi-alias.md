---
layout: post
title: "Passing all parameter arguments to irssi alias"
date: 2014-10-23 21:47:00 +03:00
updated: 2014-10-23 21:47:54 +03:00
categories: [notes]
tags: ["alias", "irssi", "self"]
excerpt: "$* expands to all arguments passed to an alias so for example, making alias /self which sends all arguments passed to it to myself using network 'Network' : /alias self /msg -Ne..."
original_url: "https://koodinpatkia.blogspot.com/2014/10/passing-all-parameter-arguments-to.html"
---

<pre>$*        expands to all arguments passed to an alias</pre><pre>&nbsp;</pre><pre>so for example, making alias /self which sends all arguments passed to it to myself using network 'Network' :</pre><pre>/alias self /msg -Network $N $*</pre>
