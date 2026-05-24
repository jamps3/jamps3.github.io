---
layout: post
title: "Clear SharePoint Designer cache"
date: 2014-08-22 17:58:00 +03:00
updated: 2014-08-22 17:58:53 +03:00
categories: [sharepoint]
tags: ["cache", "sharepoint", "sharepoint 2010"]
excerpt: "Sometimes SharePoint Designer loses touch with reality - it demands to check out files that are not checked in, refuses to check in other files and generally misbehaves. This de..."
original_url: "https://koodinpatkia.blogspot.com/2014/08/clear-sharepoint-designer-cache.html"
---

Sometimes SharePoint Designer loses touch with reality - it demands to check out files that are not checked in, refuses to check in other files and generally misbehaves. This demeanor is sometimes accompanied by this error message:<br />
<code><pre>    "Cannot perform this operation. The file is no longer checked out or has been deleted."
</pre></code><br />
Simply put, SharePoint Designer is out of sync with SharePoint and you have to delete its cache in order to rebuild it. The cache is composed of these 2 folders:<br />
<code><pre>    %APPDATA%\Microsoft\Web Server Extensions\Cache
    %USERPROFILE%\AppData\Local\Microsoft\WebsiteCache
</pre></code><br />
Just delete their contents and you are done.<br />
I found the solution <a href="http://www.myspblog.com/2011/07/clear-sharepoint-designer-cache.html">here</a>.
