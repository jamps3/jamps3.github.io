---
layout: post
title: "How to display Sharepoint List item/link in a pop-up/pop-in dialog window"
date: 2014-09-05 19:22:00 +03:00
updated: 2014-09-05 19:22:23 +03:00
categories: [sharepoint]
tags: ["popup", "sharepoint", "sharepoint 2010"]
excerpt: "Ever wondered why List items won't open in a dialog even though you have enabled \"Launch forms in a dialog?\" setting of the List? Well wonder no more, and just create the popup..."
original_url: "https://koodinpatkia.blogspot.com/2014/09/how-to-display-sharepoint-list-itemlink.html"
---

Ever wondered why List items won't open in a dialog even though you have enabled "Launch forms in a dialog?" setting of the List?<br />
Well wonder no more, and just create the popup yourself! Use this code:<br />
<code><pre>&lt;a href="javascript:OpenPopUpPage('http://mysite/Lists/Announcements/DispForm.aspx?ID={@ID}')"&nbsp; &gt;
&lt;xsl:value-of select="substring(@Title, 1, 27)" /&gt;...&lt;/a&gt;
</pre></code><br />
<br />
btw, the code includes trimming text to 27 characters and inserting "..." in the end. Works!
