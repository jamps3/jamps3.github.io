---
layout: post
title: "Weird flickering effect with HTML/CSS"
date: 2014-09-22 19:37:00 +03:00
updated: 2014-09-22 19:37:52 +03:00
categories: [web]
tags: ["bug", "css", "html", "popup", "sharepoint"]
excerpt: "Just found out that when using in-page popups, using this CSS breaks the page so that it starts flickering/strobing constantly sometimes :D html {overflow: auto;} So word of adv..."
original_url: "https://koodinpatkia.blogspot.com/2014/09/weird-flickering-effect-with-htmlcss.html"
---

Just found out that when using in-page popups, using this CSS breaks the page so that it starts flickering/strobing constantly sometimes :D<br />
<code><pre>html {overflow: auto;}
</pre></code><br />
So word of advice: don't use it :) Or use it with some other parameter than "auto".
