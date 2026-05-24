---
layout: post
title: "Passing all parameter arguments to irssi alias"
date: 2014-10-23 21:47:00 +03:00
updated: 2014-10-23 21:47:54 +03:00
categories: [notes]
tags: ["alias", "irssi", "self"]
excerpt: "$* expands to all arguments passed to an alias so for example, making alias /self which sends all arguments passed to it to myself using network 'Network' : /alias self /msg -Ne..."
original_url: "https://koodinpatkia.blogspot.com/2014/10/passing-all-parameter-arguments-to.html"
migrated: true
lang: en
---

```text
$*        expands to all arguments passed to an alias
```

```text
so for example, making alias /self which sends all arguments passed to it to myself using network 'Network' :
```

```text
/alias self /msg -Network $N $*
```

