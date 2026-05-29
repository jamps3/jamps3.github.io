---
layout: post
title: "How to format Date / DateTime fields in Sharepoint 2010 using custom xsl and ddwrt formatting"
date: 2014-09-24 15:51:00 +03:00
updated: 2014-09-24 15:51:00 +03:00
categories: ["sharepoint"]
tags: ["datetime", "ddwrt", "formatting", "sharepoint", "sharepoint 2010", "xsl"]
excerpt: "When getting Calendar items, use ddwrt:FormatDate to format Date/Time as your liking: from <xsl:value-of select=\"ddwrt:FormatDate(string(@EventDate),2057,3)\"/> to <xsl:value-of..."
original_url: "https://koodinpatkia.blogspot.com/2014/09/how-to-format-date-datetime-fields-in.html"
lang: "en"
migrated: true
---

When getting Calendar items, use ddwrt:FormatDate to format Date/Time as your liking:

```text
from <xsl:value-of select="ddwrt:FormatDate(string(@EventDate),2057,3)"/>
to <xsl:value-of select="ddwrt:FormatDate(string(@EndDate),2057,3)"/>
```

Also, you can use custom formatting with this:

```text
<xsl:variable name="monthy" select="ddwrt:FormatDateTime(string(pubDate), 1033, 'MMMM')"/>
```

More Links to help you:

<a href="http://sharethelearning.blogspot.com/2007/03/formating-dates-times-and-currency-in.html">Available locales</a>

<a href="http://blogs.msdn.com/b/joshuag/archive/2009/03/25/custom-date-formats-in-sharepoint-xsl.aspx">Custom date formats</a>

<a href="http://social.msdn.microsoft.com/Forums/office/en-US/5dad5220-1fcd-41e6-820d-880c1c738798/xsl-custom-format-datetime-column?forum=sharepointcustomizationlegacy">MSDN DateTime custom format</a>

<a href="http://msdn.microsoft.com/en-us/library/ms256099.aspx">ms:format-date Function</a>

<a href="http://sharepointnuke.blogspot.in/2010/07/xslt-date-format-dd-mmm-yyyy-using.html">XSLT Date format dd-MMM-yyyy using ddwrt:FormatDateTime</a>

<a href="http://autosponge.wordpress.com/2008/05/09/ddwrt-formatdate-and-formatdatetime/">ddwrt FormatDate and FormatDateTime</a>

<a href="http://shbdev.wordpress.com/2010/06/28/how-to-format-date-value-in-sharepoint-data-view-web-part-xslt/">How to format date value in SharePoint Data View Web Part – xslt</a>