---
layout: post
title: "Prevent BitLocker Auto-Encryption in Windows 11 Install"
date: 2026-05-27 15:11:36 +03:00
updated: 2026-05-27 15:11:36 +03:00
categories: ["Windows"]
tags: ["windows-11", "bitlocker", "encryption", "security", "tutorial"]
excerpt: "If you are doing a clean install and want to prevent Windows from automatically enabling BitLocker later."
lang: "en"
migrated: false
---

In the Command Prompt, type regedit and press Enter.
Navigate to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\BitLocker
Right-click the empty space on the right, select New > DWORD (32-bit) Value.
Name it PreventDeviceEncryption.
Double-click it and change the Value data to 1.
Close the Registry Editor and Command Prompt, then continue your installation.