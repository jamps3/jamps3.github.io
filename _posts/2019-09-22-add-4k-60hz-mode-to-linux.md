---
layout: post
title: "Add 4K 60Hz mode to Linux"
date: 2019-09-22 12:35:00 +03:00
updated: 2019-09-22 12:35:13 +03:00
categories: [linux]
tags: ["blogger-import", "linux"]
excerpt: "60Hz mode not displaying in your Display settings? No problem! We need two commands, cvt and xrandr. Step 1: Calculate a Modeline for xrandr using cvt: user@machine:~$ cvt 3840..."
original_url: "https://koodinpatkia.blogspot.com/2019/09/add-4k-60hz-mode-to-linux.html"
migrated: true
lang: en
---

60Hz mode not displaying in your Display settings? No problem!

We need two commands, cvt and xrandr.

Step 1: Calculate a Modeline for xrandr using cvt:

```text
user@machine:~$ cvt 3840 2160 60
# 3840x2160 59.98 Hz (CVT 8.29M9) hsync: 134.18 kHz; pclk: 712.75 MHz
Modeline "3840x2160_60.00"  712.75  3840 4160 4576 5312  2160 2163 2168 2237 -hsync +vsync
```
Step 2: Use xrandr to see which output your display uses:

```text
user@machine:~$ xrandr
Screen 0: minimum 320 x 200, current 3840 x 2160, maximum 16384 x 16384
DisplayPort-2 connected primary 3840x2160+0+0 (normal left inverted right x axis y axis) 640mm x 360mm
```
We can see it uses "DisplayPort-2".

Step 3: Create a new Mode with xrandr and give it a descriptive name like "3840x2160@60Hz":

```text
user@machine:~$ xrandr --newmode "3840x2160@60Hz" 712.75 3840 4160 4576 5312  2160 2163 2168 2237 -hsync +vsync
```
Step 4: Add the new Modeline to your display with xrandr:

```text
user@machine:~$ xrandr --addmode DisplayPort-2 3840x2160@60Hz
```
Step 5: Test if it works! Go to display options and choose ~60Hz. If it doesn't work or you see some artefacts we need to calculate a Mode with "reduced blanking".

Step 6: Calculate a "reduced blanking" Modeline for xrandr using cvt:

```text
user@machine:~$ cvt 3840 2160 60 -r
# 3840x2160 59.97 Hz (CVT 8.29M9-R) hsync: 133.25 kHz; pclk: 533.00 MHz
Modeline "3840x2160R"  533.00  3840 3888 3920 4000  2160 2163 2168 2222 +hsync -vsync
```
Step 7: Create a new Mode with xrandr and give it a descriptive name like "4K60Hz":

```text
user@machine:~$ xrandr --newmode "3840x2160@60Hz-R" 533.00 3840 3888 3920 4000  2160 2163 2168 2222 +hsync -vsync
```
Step 8: Add the new Modeline to your display with xrandr:

```text
user@machine:~$ xrandr --addmode DisplayPort-2 3840x2160@60Hz-R
```
 Step 9: Profit! Now you should have a working 4K resolution with 60Hz(or more).

