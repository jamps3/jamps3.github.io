---
layout: post
title: "Hide the Ribbon row in Sharepoint 2010-2013 modal box / dialog popup"
date: 2014-09-09 19:22:00 +03:00
updated: 2014-09-09 19:24:47 +03:00
categories: [sharepoint]
tags: ["dialog", "disable", "hide", "popup", "ribbon", "sharepoint", "sharepoint 2010", "sharepoint 2013"]
excerpt: "Insert the following 3 lines of CSS code into your page: . ms - dialog #s4-ribbonrow { display : none ; } Done!"
original_url: "https://koodinpatkia.blogspot.com/2014/09/hide-ribbon-row-in-sharepoint-2010-2013.html"
migrated: true
lang: en
---

Insert the following 3 lines of CSS code into your page:

```text
.ms-dialog #s4-ribbonrow { 
    display: none;
}
```Done!

