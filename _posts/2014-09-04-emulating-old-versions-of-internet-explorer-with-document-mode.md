---
layout: post
title: "Emulating old versions of Internet Explorer with Document Mode"
date: 2014-09-04 18:47:00 +03:00
updated: 2014-09-04 18:47:30 +03:00
categories: [linux]
tags: ["blogger-import", "linux", "web"]
excerpt: "Press F12 to reach Developer toolbar and scroll down on the left to reach Emulation(or press CTRL+8). The Document Mode selection lets you choose how Internet Explorer interpret..."
original_url: "https://koodinpatkia.blogspot.com/2014/09/emulating-old-versions-of-internet.html"
migrated: true
lang: en
---

Press F12 to reach Developer toolbar and scroll down on the left to reach Emulation(or press CTRL+8).

The Document Mode selection lets you choose how Internet Explorer interprets the page, and can be useful for diagnosing compatibility issues. There will be a (Default) next to the mode being used by the page. You can choose another mode, the number indicates the version of Internet Explorer. Each mode makes a series of changes to the browser's behavior so that it closely emulates the older browser version. The page reloads when you choose a new mode so that the web server and client-side markup is reinterpreted in the new mode.

Changes made to the Document Mode in F12 Developer Tools apply only for the duration of the browser session; when you close the browser and return to the site it will be in the default mode again.

Starting with IE11, Edge mode is the preferred document mode; it represents the highest support for modern standards available to the browser.

