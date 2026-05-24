---
layout: post
title: "Centered fixed width design in SharePoint 2010 with CSS - The best way"
date: 2014-08-06 14:36:00 +03:00
updated: 2014-08-21 18:08:00 +03:00
categories: [web]
tags: ["centered", "css", "fixed width", "page", "sharepoint 2010"]
excerpt: "Most of the tutorials available on the 'net don't respect the ribbon and stuff it into a design that has a fixed width. This is the fastest way to get a fixed width design and n..."
original_url: "https://koodinpatkia.blogspot.com/2014/08/centered-fixed-width-design-in.html"
---

Most of the tutorials available on the 'net don't respect the ribbon and stuff it into a design that has a fixed width. This is the fastest way to get a fixed width design and needs only the following CSS code and is flexible to be changed to any desired width.<br />
<blockquote><code><pre>div.s4-title.s4-lp,
body #s4-mainarea,
#s4-topheader2,
#s4-statusbarcontainer {
width: 960px;
margin: auto;
padding: 0px;
float: none;
background-image: none;
background-color: white;
}
</pre></code></blockquote><br />
To get the fixed width design working with the v4.master some classes needs to be added.<br />
<code><pre>&lt;div id="s4-workspace"&gt;
</pre></code><br />
Needs to be changed to:<br />
<code><pre>&lt;div id="s4-workspace" class="s4-nosetwidth"&gt;
</pre></code><br />
And the second html element needs to be altered:<br />
<code><pre>&lt;div id="s4-titlerow" class="s4-pr s4-notdlg s4-titlerowhidetitle"&gt;
</pre></code><br />
This needs to be changed to:<br />
<code><pre>&lt;div id="s4-titlerow" class="s4-pr s4-notdlg s4-titlerowhidetitle s4-nosetwidth"&gt;
</pre></code><br />
By adding the s4-nosetwidth style class SharePoint won’t assign the inline style property for width and the design will stay centered.<br />
<br />
The size of the design could be changed to any size just by simply modifying the width property. Remember always respect the size of the ribbon and let it live outside your design for easy editing.<br />
<br />
<a href="https://www.nothingbutsharepoint.com/sites/eusp/pages/centered-fixed-width-design-in-sharepoint-2010-the-fast-way.aspx">Original post here</a>
