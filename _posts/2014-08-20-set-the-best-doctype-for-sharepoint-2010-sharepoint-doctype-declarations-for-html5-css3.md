---
layout: post
title: "Set the best DOCTYPE for Sharepoint 2010, Sharepoint doctype declarations for HTML5 & CSS3"
date: 2014-08-20 19:46:00 +03:00
updated: 2014-09-08 18:07:24 +03:00
categories: [web]
tags: ["doctype", "html", "sharepoint", "sharepoint 2010"]
excerpt: "When working with advanced Sharepoint designs, one usually wants to change the document type to allow for more relaxed syntax and opportunities. On the top of your Master page,..."
original_url: "https://koodinpatkia.blogspot.com/2014/08/set-best-doctype-for-sharepoint-2010.html"
---

When working with advanced Sharepoint designs, one usually wants to change the document type to allow for more relaxed syntax and opportunities.<br />
<br />
On the top of your Master page, add this:<br />
<code><pre>&lt;!DOCTYPE html&gt;</pre></code><br />
It changes the document type to a HTML5-compliant mode.<br />
Remember to change the meta tag "X-UA-Compatible" to a newer version, or delete it completely:<br />
<code><pre>&lt;meta http-equiv="X-UA-Compatible" content="IE=8"/&gt;
</pre></code><br />
Otherwise Internet Explorer will render the page in IE8 compatibility mode, so CSS3 & HTML5 won't work.<br />
<br />
When using an older environment, this DOCTYPE declaration seems to be the best and also the most relaxed: HTML 4.0 Transitional in Standards Mode<br />
<br />
So, type the following line to the top of your Master page, where the previous setting is, overwriting it:<br />
<code class="prettyprint"><pre>&lt;!DOCTYPE html PUBLIC "-//W3C//DTD html 4.01 Transitional//EN" 
"http://www.w3.org/TR/html4/loose.dtd"&gt;
</pre></code><br />
Remember, don't change the DOCTYPE in your regular pages, only in the Master page! Because it doesn't work that way, it has to be on top of the rendered(master) page.<br />
<br />
EDIT: Sometimes it might be best NOT to include any doctype definition, that might break old IE. See more info in this link:<br />
<a href="http://techtrainingnotes.blogspot.fr/2009/01/sharepoint-doctype-notes.html">Lots of more info & experience here</a>.
