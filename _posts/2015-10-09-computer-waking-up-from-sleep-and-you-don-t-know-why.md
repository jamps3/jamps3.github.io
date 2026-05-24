---
layout: post
title: "Computer waking up from sleep and you don't know why?"
date: 2015-10-09 15:37:00 +03:00
updated: 2015-10-09 15:37:28 +03:00
categories: [windows]
tags: ["blogger-import", "windows"]
excerpt: "Controlling which devices will wake the computer out of sleep: If your computer keeps waking up from standby/sleep, here is how to figure out what causes it. 1) Open a command p..."
original_url: "https://koodinpatkia.blogspot.com/2015/10/computer-waking-up-from-sleep-and-you.html"
---

<h2>
Controlling which devices will wake the computer out of sleep:</h2>
If your computer keeps waking up from standby/sleep, here is how to figure out what causes it.<br />
<br />
1) Open a command prompt with Administrator privileges and run the command:<br />
<blockquote class="tr_bq">
powercfg -devicequery wake_armed</blockquote>
2) You see a list of devices that have permission to wake up your computer. You can disable each of these devices one by one until you find the
one that is waking up the computer by running this command with the name of the device listed in quotes:<br />
<blockquote class="tr_bq">
powercfg -devicedisablewake "device name"</blockquote>
Once you find the one that is causing problems, you can re-enable
the others:<br />
<blockquote class="tr_bq">
powercfg -deviceenablewake "device name"</blockquote>
You can get a more detailed list of devices capable of waking up your computer with the command:<br />
<blockquote class="tr_bq">
powercfg -devicequery wake_from_any</blockquote>
<br />
I had my LAN-card causing the problem, and got it disabled by running this:<br />
<blockquote class="tr_bq">
&nbsp;powercfg -devicedisablewake "Realtek PCIe GBE Family Controller"</blockquote>
You may have a problem with your mouse moving a little, which causes the computer to wake up. You can either turn the mouse upside down, or disable it's ability to wake up the computer for good.
