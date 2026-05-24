---
layout: post
title: "Move/set Firefox cache location"
date: 2014-04-13 17:59:00 +03:00
updated: 2014-07-07 13:02:51 +03:00
categories: [web]
tags: ["cache", "firefox", "location"]
excerpt: "You can do this by creating a new hidden preference. Type about:config into the location bar and press enter Accept the warning message that appears, you will be taken to a list..."
original_url: "https://koodinpatkia.blogspot.com/2014/04/moveset-firefox-cache-location.html"
---

You can do this by creating a new hidden preference.
<br />
<br />
<li>Type about:config into the location bar and press enter</li>
<li>Accept the warning message that appears, you will be taken to a list of preferences</li>
<li>Right-click somewhere in the list and select "New &gt; String"</li>
<li>For the name of the preference type browser.cache.disk.parent_directory</li>
<li>For its value type the path to where you want to store the cache, for example d:\fftemp</li>
<li>Next locate the preference browser.cache.disk.enable, it must be set to true, if it is not, double-click on it to change its value</li>
<li>Set the size of the cache to something like 32000 to 512000 by setting browser.cache.disk.capacity (32-512MB)</li>
<br />
For more information on this see: <a href="https://support.mozilla.org/en-US/questions/768867" target="_blank">https://support.mozilla.org/en-US/questions/768867</a>
