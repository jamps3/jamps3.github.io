---
layout: post
title: "Simple Menu with HTML, CSS & jQuery"
date: 2012-11-14 21:35:00 +02:00
updated: 2014-01-17 11:42:37 +02:00
categories: [web]
tags: ["css", "html", "jquery", "menu", "simple"]
excerpt: "Here we have a simple menu and CSS Sprite styling example. HTML: Info Updates Media Downloads Forums CSS: /* Custom Menu */ ul { list-style-type: none; } ul#nav li, ul#nav li a..."
original_url: "https://koodinpatkia.blogspot.com/2012/11/simple-menu-with-html-css-jquery.html"
---

Here we have a simple menu and CSS Sprite styling example.

HTML:
<code class="prettyprint">
<ul id="nav">
 <li class="info"><a href="#">Info</a></li>
 <li class="updates"><a href="#">Updates</a></li>
 <li class="media"><a href="#">Media</a></li>
 <li class="downloads"><a href="#">Downloads</a></li>
 <li class="forums"><a href="#">Forums</a></li>
</ul>
</code>
CSS:
<code class="prettyprint">
/* Custom Menu */ ul { list-style-type: none; } ul#nav li, ul#nav li a { background: url('../images/oldmenuexamplesprite.png') no-repeat left top; height: 31px; } /* We give the

and the sprite as the background and set the button dimensions */ ul#nav li { float: left; border: 0px solid #243e3b; border-left: none; } ul#nav li a { display: block; text-indent: -9999px; } ul#nav li.info a { width: 93px; } /* Here we set the button widths. */ ul#nav li.updates a { width: 111px; } ul#nav li.media a { width: 83px; } ul#nav li.downloads a { width: 138px; } ul#nav li.forums a { width: 140px; } ul#nav li.info a { background-position: 0px 0px; } /* Here we set the background/sprite position */ ul#nav li.updates a { background-position: -93px 0px; } ul#nav li.media a { background-position: -204px 0px; } ul#nav li.downloads a { background-position: -287px 0px; } ul#nav li.forums a { background-position: -425px 0px; } ul#nav li.info a:hover { background-position: 0px -34px; } /* And now the hover background-position position */ ul#nav li.updates a:hover { background-position: -93px -34px; } ul#nav li.media a:hover { background-position: -204px -34px; } ul#nav li.downloads a:hover { background-position: -287px -34px; } ul#nav li.forums a:hover { background-position: -425px -34px; }
</code>
jQuery:
<code class="prettyprint">
(function ($) { /* Needed for Drupal 7 */

 $(document).ready(function(){ 

 //Set the anchor link opacity to 0 and begin hover function
 $("ul#nav li a").css({"opacity" : 0}).hover(function(){ 

 //Fade to an opacity of 1 at a speed of 200ms
 $(this).stop().animate({"opacity" : 1}, 200); 

 //On mouse-off
 }, function(){

 //Fade to an opacity of 0 at a speed of 100ms
 $(this).stop().animate({"opacity" : 0}, 100); 

 });

 //Add more jQuery functionality here...

});
  
})(jQuery); /* Needed for Drupal 7 */
</code>
