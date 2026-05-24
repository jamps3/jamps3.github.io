---
layout: post
title: "Use jQuery CDN with fallback"
date: 2012-11-15 00:47:00 +02:00
updated: 2014-06-18 18:01:44 +03:00
categories: [web]
tags: ["cdn", "fallback", "jquery"]
excerpt: "Use jQuery from CDN, because it is usually cached. Always use fallback (Sometimes Google fails). <script type=\"text/javascript\" src=\"http://ajax.googleapis.com/ajax/libs/jquery/..."
original_url: "https://koodinpatkia.blogspot.com/2012/11/use-jquery-cdn-with-fallback.html"
---

Use jQuery from CDN, because it is usually cached.
Always use fallback (Sometimes Google fails).
<br />
<code class="prettyprint">
&lt;script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.2.6/jquery.min.js"&gt;&lt;/script&gt;<br />
&lt;script type="text/javascript"&gt;<br />
if (typeof jQuery == 'undefined')<br />
{<br />
document.write(unescape("%3Cscript src='/path/to/your/jquery' type='text/javascript'%3E%3C/script%3E"));<br />
}<br />
&lt;/script&gt;<br />
</code>
