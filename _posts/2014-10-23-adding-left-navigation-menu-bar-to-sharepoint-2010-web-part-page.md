---
layout: post
title: "Adding left navigation menu bar to Sharepoint 2010 Web Part page"
date: 2014-10-23 17:43:00 +03:00
updated: 2014-10-23 17:46:17 +03:00
categories: [sharepoint]
tags: ["blogger-import", "sharepoint", "web"]
excerpt: "Open your Web Part page in Sharepoint Designer. Step 1 – Remove CSS Around line 34 you will find a code block like the one below <SharePoint:UIVersionedContent ID=\"WebPartPageHi..."
original_url: "https://koodinpatkia.blogspot.com/2014/10/step-1-remove-css-around-line-34-you.html"
---

<span class="Apple-style-span" style="font-size: 19px;">Open your Web Part page in Sharepoint Designer.</span><span class="Apple-style-span" style="font-size: 19px; font-weight: bold;"> </span><br />
<br />
<span class="Apple-style-span" style="font-size: 19px; font-weight: bold;">Step 1 – Remove CSS</span><br />
Around line 34 you will find a code block like the one below<br />
<br />
<code>&lt;SharePoint:UIVersionedContent ID="WebPartPageHideQLStyles" UIVersion="4" runat="server"&gt;<br />
&lt;ContentTemplate&gt;<br />
&lt;style type="text/css"&gt;<br />
body #s4-leftpanel {<br />
display:none;<br />
}<br />
.s4-ca {<br />
margin-left:0px;<br />
}<br />
&lt;/style&gt;<br />
&lt;/ContentTemplate&gt;<br />
&lt;/SharePoint:UIVersionedContent&gt;</code><br />
<br />
Delete this code block.<br />
<span class="Apple-style-span" style="font-size: 19px; font-weight: bold;"><br />
</span><br />
<span class="Apple-style-span" style="font-size: 19px; font-weight: bold;">Step 2 – Remove the overrides for the left column</span><br />
<br />
Further down you will find three lines which prevents the left column for rendering.<br />
<code><br />
&lt;asp:Content ContentPlaceHolderId="PlaceHolderPageImage" runat="server"&gt;&lt;/asp:Content&gt;<br />
&lt;asp:Content ContentPlaceHolderId="PlaceHolderNavSpacer" runat="server"&gt;&lt;/asp:Content&gt;<br />
&lt;asp:Content ContentPlaceHolderId="PlaceHolderLeftNavBar" runat="server"&gt;&lt;/asp:Content&gt;<br />
</code><br />
Remove all three lines.<br />
<br />
<span class="Apple-style-span" style="font-size: 19px; font-weight: bold;">Step 3 – Save the page</span>
