---
layout: post
title: "How to trim/limit text length to a specified number of characters in Sharepoint 2010"
date: 2014-09-05 19:29:00 +03:00
updated: 2014-09-05 19:29:38 +03:00
categories: [sharepoint]
tags: ["length", "sharepoint", "sharepoint 2010", "string", "text", "trim"]
excerpt: "Here I have specified 27 as the maximum length, plus three dots after the string. <xsl:value-of select=\"substring(@Title, 1, 27)\" />..."
original_url: "https://koodinpatkia.blogspot.com/2014/09/how-to-trimlimit-text-length-to.html"
migrated: true
lang: en
---

Here I have specified 27 as the maximum length, plus three dots after the string.

```text
<xsl:value-of select="substring(@Title, 1, 27)" />...
```

