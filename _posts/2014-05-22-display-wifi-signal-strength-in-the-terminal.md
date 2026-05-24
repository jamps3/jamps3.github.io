---
layout: post
title: "Display WiFi signal strength in the terminal"
date: 2014-05-22 01:45:00 +03:00
updated: 2014-07-01 11:15:12 +03:00
categories: [android]
tags: ["signal", "terminal", "wifi", "wlan"]
excerpt: "You can run this command: watch -n 1 \"awk 'NR==3 {print \\\"WiFi Signal Strength = \\\" \\$3 \\\"00 %\\\"}''' /proc/net/wireless\" This command has also the same function, with more info:..."
original_url: "https://koodinpatkia.blogspot.com/2014/05/to-display-wifi-signal-strength-in.html"
migrated: true
lang: en
---

You can run this command:

watch -n 1 "awk 'NR==3 {print \"WiFi Signal Strength = \" \$3 \"00 %\"}''' /proc/net/wireless"

This command has also the same function, with more info:

watch -n 1 cat /proc/net/wireless

