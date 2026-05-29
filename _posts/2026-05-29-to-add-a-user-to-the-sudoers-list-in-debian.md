---
layout: post
title: "To add a user to the sudoers list in Debian"
date: 2026-05-29 03:09:59 +03:00
updated: 2026-05-29 03:09:59 +03:00
categories: ["Linux"]
tags: ["Linux", "Debian", "Sudo"]
excerpt: "To add a user to the sudoers list in Debian, the most straightforward and secure method is to add the user to the sudo group using the usermod command."
lang: "en"
migrated: false
---

To add a user to the sudoers list in Debian, the most straightforward and secure method is to add the user to the sudo group using the usermod command.

The Easiest Method (Using the Sudo Group)
Log in as the root user or another user who already has sudo privileges.Run the following command (replace username with the actual name of your user)

:bash
usermod -aG sudo username

Log out of the current session and log back in (or use the command su - username) for the group change to take effect.