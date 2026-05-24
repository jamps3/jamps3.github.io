---
layout: post
title: "@font-face definition for multiple browsers and devices using FontSquirrel"
date: 2014-08-08 14:40:00 +03:00
updated: 2014-08-21 18:09:15 +03:00
categories: [web]
tags: ["css", "fonts", "web"]
excerpt: "1) Download fonts to your server from FontSquirrel 2) Add these CSS definitions, change the path and font filenames if needed: /*-- Font Definitions, free Roboto font from FontS..."
original_url: "https://koodinpatkia.blogspot.com/2014/08/font-face-definition-for-multiple.html"
migrated: true
lang: en
---

1) Download fonts to your server from FontSquirrel

2) Add these CSS definitions, change the path and font filenames if needed:

```text
/*-- Font Definitions, free Roboto font from FontSquirrel - works with all major browsers--*/
@font-face {
    font-family: 'robotoregular';
    src: url('fonts/Roboto-Regular-webfont.eot');
    src: url('fonts/Roboto-Regular-webfont.eot?#iefix') format('embedded-opentype'),
         url('fonts/Roboto-Regular-webfont.woff') format('woff'),
         url('fonts/Roboto-Regular-webfont.ttf') format('truetype'),
         url('fonts/Roboto-Regular-webfont.svg#robotoregular') format('svg');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'robotolight';
    src: url('fonts/Roboto-Light-webfont.eot');
    src: url('fonts/Roboto-Light-webfont.eot?#iefix') format('embedded-opentype'),
         url('fonts/Roboto-Light-webfont.woff') format('woff'),
         url('fonts/Roboto-Light-webfont.ttf') format('truetype'),
         url('fonts/Roboto-Light-webfont.svg#robotolight') format('svg');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'robotothin';
    src: url('fonts/Roboto-Thin-webfont.eot');
    src: url('fonts/Roboto-Thin-webfont.eot?#iefix') format('embedded-opentype'),
         url('fonts/Roboto-Thin-webfont.woff') format('woff'),
         url('fonts/Roboto-Thin-webfont.ttf') format('truetype'),
         url('fonts/Roboto-Thin-webfont.svg#robotothin') format('svg');
    font-weight: normal;
    font-style: normal;
}
```

3) Done! It was so easy!

Here I have used 3 different weights of the same Roboto font. You can manage with only one and use the font-weight property, but I heard it's sometimes uglier method. This method ensures the best quality.

Btw I compared the same Roboto font from Google fonts and FontSquirrel:

Google Roboto is ~125kB

FontSquirrel Roboto is ~25kB

