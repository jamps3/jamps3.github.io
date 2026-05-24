---
layout: post
title: "Add custom CSS file to a Sharepoint 2010 site"
date: 2014-08-05 19:50:00 +03:00
updated: 2014-08-21 18:11:03 +03:00
categories: [sharepoint]
tags: ["sharepoint 2010"]
excerpt: "Open up your current masterpage. This is usually v4.master by default, and always located in the “_catalogs/masterpage” directory. Remember to make a copy of it and edit the cop..."
original_url: "https://koodinpatkia.blogspot.com/2014/08/add-custom-css-file-to-sharepoint-2010.html"
migrated: true
lang: en
---

Open up your current masterpage. This is usually v4.master by default,  and always located in the “_catalogs/masterpage” directory. Remember to make a copy of it and edit the copy! Then set it as your default Master page.

Right before the

```text
<asp:contentplaceholder id="PlaceHolderAdditionalPageHead" runat="server">
</asp:contentplaceholder>
```

tag, put the following line of code to include a reference to your custom CSS file.

```text
<sharepoint:cssregistration after="corev4.css" name="&lt;% $SPUrl:~SiteCollection/Style Library/Custom/styles.css %&gt;" runat="server">
</sharepoint:cssregistration>
```

Done!

