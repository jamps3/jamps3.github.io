---
layout: post
title: "Adding left navigation menu bar to Sharepoint 2010 Web Part page"
date: 2014-10-23 17:43:00 +03:00
updated: 2014-10-23 17:43:00 +03:00
categories: ["sharepoint"]
tags: ["blogger-import", "sharepoint", "web"]
excerpt: "Open your Web Part page in Sharepoint Designer. Step 1 – Remove CSS Around line 34 you will find a code block like the one below <SharePoint:UIVersionedContent ID=\"WebPartPageHi..."
original_url: "https://koodinpatkia.blogspot.com/2014/10/step-1-remove-css-around-line-34-you.html"
lang: "en"
migrated: true
---

Open your Web Part page in Sharepoint Designer. 

Step 1 – Remove CSS

Around line 34 you will find a code block like the one below

```text
<SharePoint:UIVersionedContent ID="WebPartPageHideQLStyles" UIVersion="4" runat="server">

<ContentTemplate>

<style type="text/css">

body #s4-leftpanel {

display:none;

}

.s4-ca {

margin-left:0px;

}

</style>

</ContentTemplate>

</SharePoint:UIVersionedContent>
```

Delete this code block.

Step 2 – Remove the overrides for the left column

Further down you will find three lines which prevents the left column for rendering.

```text
<asp:Content ContentPlaceHolderId="PlaceHolderPageImage" runat="server"></asp:Content>

<asp:Content ContentPlaceHolderId="PlaceHolderNavSpacer" runat="server"></asp:Content>

<asp:Content ContentPlaceHolderId="PlaceHolderLeftNavBar" runat="server"></asp:Content>
```

Remove all three lines.

Step 3 – Save the page