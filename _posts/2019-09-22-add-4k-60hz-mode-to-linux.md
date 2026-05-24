---
layout: post
title: "Add 4K 60Hz Mode to Linux"
date: 2019-09-22 12:00:00 +0300
categories: [linux]
tags: [linux, xrandr, display, 4k, monitor]
excerpt: "How to manually add a missing 4K 60Hz display mode in Linux using cvt and xrandr."
original_url: "https://koodinpatkia.blogspot.com/2019/09/add-4k-60hz-mode-to-linux.html"
---

Sometimes Linux does not automatically expose every display mode your monitor and GPU can use.
For example, 4K may appear only at 30Hz even when 60Hz should work.

This note shows how to manually add a 3840x2160 60Hz mode using `cvt` and `xrandr`.

<!--more-->

## 1. Create a modeline

```bash
cvt 3840 2160 60
```

Example output:

```bash
# 3840x2160 59.98 Hz (CVT) hsync: 134.18 kHz; pclk: 712.75 MHz
Modeline "3840x2160_60.00" 712.75 3840 4160 4576 5312 2160 2163 2168 2237 -hsync +vsync
```

## 2. Check your display output name

```bash
xrandr
```

Look for the connected display name, for example `HDMI-1` or `DP-1`.

## 3. Add the new mode

```bash
xrandr --newmode "3840x2160_60.00" 712.75 3840 4160 4576 5312 2160 2163 2168 2237 -hsync +vsync
```

## 4. Attach the mode to the output

Replace `HDMI-1` with your actual output name:

```bash
xrandr --addmode HDMI-1 "3840x2160_60.00"
```

## 5. Enable the mode

```bash
xrandr --output HDMI-1 --mode "3840x2160_60.00"
```

## Notes

If the screen goes black, wait a few seconds or switch to a TTY with `Ctrl + Alt + F3`.

{% if page.original_url %}
> Originally published on the old Koodinpätkiä blog: {{ page.original_url }}
{% endif %}
