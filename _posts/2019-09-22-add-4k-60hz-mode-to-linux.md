---
layout: post
title: "Add 4K 60Hz mode to Linux"
date: 2019-09-22 12:35:00 +03:00
updated: 2019-09-22 12:35:13 +03:00
categories: [linux]
tags: ["blogger-import", "linux"]
excerpt: "60Hz mode not displaying in your Display settings? No problem! We need two commands, cvt and xrandr. Step 1: Calculate a Modeline for xrandr using cvt: user@machine:~$ cvt 3840..."
original_url: "https://koodinpatkia.blogspot.com/2019/09/add-4k-60hz-mode-to-linux.html"
---

60Hz mode not displaying in your Display settings? No problem!<br />
<br />
We need two commands, cvt and xrandr.<br />
<br />
Step 1: Calculate a Modeline for xrandr using cvt:<br />
<blockquote class="tr_bq">
user@machine:~$ cvt 3840 2160 60<br /># 3840x2160 59.98 Hz (CVT 8.29M9) hsync: 134.18 kHz; pclk: 712.75 MHz<br />Modeline "3840x2160_60.00"&nbsp; 712.75&nbsp; 3840 4160 4576 5312&nbsp; 2160 2163 2168 2237 -hsync +vsync</blockquote>
Step 2: Use xrandr to see which output your display uses:<br />
<blockquote class="tr_bq">
user@machine:~$ xrandr<br />Screen 0: minimum 320 x 200, current 3840 x 2160, maximum 16384 x 16384<br />DisplayPort-2 connected primary 3840x2160+0+0 (normal left inverted right x axis y axis) 640mm x 360mm </blockquote>
We can see it uses "DisplayPort-2".<br />
<br />
Step 3: Create a new Mode with xrandr and give it a descriptive name like "3840x2160@60Hz":<br />
<blockquote class="tr_bq">
user@machine:~$ xrandr --newmode "3840x2160@60Hz" 712.75 3840 4160 4576 5312&nbsp; 2160 2163 2168 2237 -hsync +vsync</blockquote>
Step 4: Add the new Modeline to your display with xrandr:<br />
<blockquote class="tr_bq">
user@machine:~$ xrandr --addmode DisplayPort-2 3840x2160@60Hz</blockquote>
Step 5: Test if it works! Go to display options and choose ~60Hz. If it doesn't work or you see some artefacts we need to calculate a Mode with "reduced blanking".<br />
<br />
Step 6: Calculate a "reduced blanking" Modeline for xrandr using cvt:<br />
<blockquote class="tr_bq">
user@machine:~$ cvt 3840 2160 60 -r<br /># 3840x2160 59.97 Hz (CVT 8.29M9-R) hsync: 133.25 kHz; pclk: 533.00 MHz<br />Modeline "3840x2160R"&nbsp; 533.00&nbsp; 3840 3888 3920 4000&nbsp; 2160 2163 2168 2222 +hsync -vsync</blockquote>
Step 7: Create a new Mode with xrandr and give it a descriptive name like "4K60Hz":<br />
<blockquote class="tr_bq">
user@machine:~$ xrandr --newmode "3840x2160@60Hz-R" 533.00 3840 3888 3920 4000&nbsp; 2160 2163 2168 2222 +hsync -vsync </blockquote>
Step 8: Add the new Modeline to your display with xrandr:<br />
<blockquote class="tr_bq">
user@machine:~$ xrandr --addmode DisplayPort-2 3840x2160@60Hz-R</blockquote>
&nbsp;Step 9: Profit! Now you should have a working 4K resolution with 60Hz(or more).
