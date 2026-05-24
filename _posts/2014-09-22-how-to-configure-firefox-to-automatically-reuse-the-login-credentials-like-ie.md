---
layout: post
title: "How to configure Firefox to automatically reuse the login credentials like IE"
date: 2014-09-22 15:22:00 +03:00
updated: 2014-09-22 15:22:57 +03:00
categories: [web]
tags: ["automatic", "credentials", "firefox", "ie", "login", "ntlm"]
excerpt: "You need to enable NTLM Configuration within FireFox. It is very simple to do and should solve your problem: Open Firefox and type “about:config” in the address bar. (without th..."
original_url: "https://koodinpatkia.blogspot.com/2014/09/how-to-configure-firefox-to.html"
---

You need to enable NTLM Configuration within FireFox. It is very simple to do and should solve your problem:<br />
<br />
    Open Firefox and type “about:config” in the address bar. (without the quotes of course)<br />
    In the ‘Filter’ field type the following “network.automatic-ntlm-auth.trusted-uris”<br />
    Double click the name of the preference that we just searched for<br />
<br />
    Enter the URLs of the sites you wish to pass NTLM auth info to in the form of:<br />
<br />
    http://intranet.company.com,http://email.company.lan<br />
<br />
    Notice that you can use a comma separated list in this field.
