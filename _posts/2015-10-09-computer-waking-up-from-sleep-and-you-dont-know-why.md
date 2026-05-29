---
layout: post
title: "Computer waking up from sleep and you don't know why?"
date: 2015-10-09 15:37:00 +03:00
updated: 2015-10-09 15:37:00 +03:00
categories: ["Windows"]
tags: ["blogger-import", "windows"]
excerpt: "Controlling which devices will wake the computer out of sleep: If your computer keeps waking up from standby/sleep, here is how to figure out what causes it. 1) Open a command p..."
original_url: "https://koodinpatkia.blogspot.com/2015/10/computer-waking-up-from-sleep-and-you.html"
lang: "en"
migrated: true
---

## Controlling which devices will wake the computer out of sleep:

If your computer keeps waking up from standby/sleep, here is how to figure out what causes it.

1) Open a command prompt with Administrator privileges and run the command:

```text
powercfg -devicequery wake_armed
```
2) You see a list of devices that have permission to wake up your computer. You can disable each of these devices one by one until you find the
one that is waking up the computer by running this command with the name of the device listed in quotes:

```text
powercfg -devicedisablewake "device name"
```
Once you find the one that is causing problems, you can re-enable
the others:

```text
powercfg -deviceenablewake "device name"
```
You can get a more detailed list of devices capable of waking up your computer with the command:

```text
powercfg -devicequery wake_from_any
```

I had my LAN-card causing the problem, and got it disabled by running this:

```text
powercfg -devicedisablewake "Realtek PCIe GBE Family Controller"
```
You may have a problem with your mouse moving a little, which causes the computer to wake up. You can either turn the mouse upside down, or disable it's ability to wake up the computer for good.