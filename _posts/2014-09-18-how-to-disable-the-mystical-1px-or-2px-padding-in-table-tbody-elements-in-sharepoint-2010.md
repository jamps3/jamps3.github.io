---
layout: post
title: "How to disable the mystical 1px or 2px padding in table / tbody elements in Sharepoint 2010"
date: 2014-09-18 16:55:00 +03:00
updated: 2014-09-18 16:55:39 +03:00
categories: [web]
tags: ["bug", "css", "padding", "sharepoint", "sharepoint 2010", "table"]
excerpt: "Ever wonder, why tables get mystically some 1-2px padding around them? And any Developer console(F12) or Firebug won't show you why? Well here's why. I guess Sharepoint(or Webki..."
original_url: "https://koodinpatkia.blogspot.com/2014/09/how-to-disable-mystical-1px-or-2px.html"
migrated: true
lang: en
---

Ever wonder, why tables get mystically some 1-2px padding around them? And any Developer console(F12) or Firebug won't show you why?

Well here's why. I guess Sharepoint(or Webkit) mystically adds a 1px invisible border around tables. Here is how to disable it with CSS:

```text
table { border-collapse: collapse!important;}
```

