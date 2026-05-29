---
layout: post
title: "To restore the default permissions for the Windows hosts file"
date: 2026-05-30 02:43:17 +03:00
updated: 2026-05-30 02:43:17 +03:00
categories: ["Windows"]
tags: ["Windows", "permissions"]
excerpt: "To restore the default permissions for the Windows hosts file, you need to reset its Access Control List (ACL) using the built-in icacls tool. This will force the file to inherit the default system folder permissions (which restrict standard users from writing to it)."
lang: "en"
migrated: false
---

To restore the default permissions for the Windows hosts file, you need to reset its Access Control List (ACL) using the built-in icacls tool. This will force the file to inherit the default system folder permissions (which restrict standard users from writing to it).
How to Reset the Permissions
Open the Start menu, type cmd, right-click Command Prompt, and select Run as administrator.
Run the following command and press Enter:
```Text
icacls "C:\Windows\System32\drivers\etc\hosts" /reset
```
A successful message will read: successfully processed 1 files; Failed processing 0 files.
How to Fix Ownership (If Access is Denied)
If you get an "Access is denied" error when attempting to reset permissions, you may need to take ownership of the file first:
Right-click the hosts file (located at C:\Windows\System32\drivers\etc) and select Properties.
Switch to the Security tab and click Advanced at the bottom.
Next to "Owner," click the Change button.
Type Administrators into the object name box and click Check Names, then click OK.
Check the box for Replace owner on subcontainers and objects if it's visible, then click Apply and OK.
Close out of Properties entirely, re-open them, and try running the icacls command in the Command Prompt again.