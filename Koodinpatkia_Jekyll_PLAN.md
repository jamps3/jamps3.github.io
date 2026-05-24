# PLAN.md — Jekyll Blog for Koodinpätkiä / Code Bits

## 1. Project goal

Implement a lightweight Jekyll-powered blog for the existing GitHub Pages site.

The blog should replace or complement the old Blogger site `koodinpatkia.blogspot.com` with a clean, maintainable Markdown workflow:

- New posts are added by creating `.md` files in `_posts/`.
- No manual `posts.json` index is required.
- GitHub Pages/Jekyll automatically discovers and builds posts.
- The blog should feel suitable for short technical notes, code snippets, fixes, commands, experiments, and old migrated posts.
- The implementation must be easy to maintain manually in VS Code/GitHub.
- Avoid fragile or unsupported plugins.

Primary user workflow:

```txt
1. Create _posts/YYYY-MM-DD-post-title.md
2. Write Markdown with front matter
3. Commit + push
4. GitHub Pages rebuilds the blog
```

---

## 2. Important constraints

### 2.1 Hosting target

Target platform: GitHub Pages, likely under `jamps3.github.io`.

Use Jekyll features that are compatible with GitHub Pages.

Do not require:

- PHP
- Node.js build pipeline
- database
- server-side search
- WordPress
- Blogger API
- custom backend

### 2.2 Windows-friendly development

The user primarily uses Windows 11 and VS Code.

Jekyll local setup on native Windows can be inconvenient. Therefore:

- The site must work without local preview.
- Local preview should be optional.
- If local preview instructions are added, prefer WSL or Docker as the recommended path.
- Do not make the implementation depend on local Ruby setup unless absolutely necessary.

### 2.3 Plugin policy

Use no custom plugins.

Allowed/safe features:

- Jekyll layouts
- Liquid templates
- Markdown posts
- front matter
- includes
- Sass/CSS or plain CSS
- Rouge syntax highlighting
- GitHub Pages-supported plugins only, if already used by the site

Avoid plugins that GitHub Pages cannot build directly.

---

## 3. Recommended URL structure

Keep a simple visible blog entry page:

```txt
/blog.html
```

Generated post URLs should be readable and stable:

```txt
/blog/2026/05/24/add-4k-60hz-mode-to-linux/
```

Recommended `_config.yml` permalink:

```yml
permalink: /blog/:year/:month/:day/:title/
```

Reasoning:

- `/blog.html` is easy to link from the existing site navigation.
- Individual post URLs are clean and future-proof.
- The URL structure separates blog posts from other portfolio pages.

---

## 4. Target file structure

Implement or adapt this structure:

```txt
/
├─ _config.yml
├─ blog.html
├─ archive.html
├─ tags.html
├─ _layouts/
│  ├─ default.html
│  └─ post.html
├─ _includes/
│  ├─ blog-card.html
│  ├─ tag-list.html
│  └─ post-meta.html
├─ _posts/
│  ├─ 2019-09-22-add-4k-60hz-mode-to-linux.md
│  └─ 2026-05-24-example-code-note.md
├─ _drafts/
│  └─ example-draft.md
├─ assets/
│  ├─ css/
│  │  └─ blog.css
│  └─ js/
│     └─ blog.js
└─ assets/blog/
   └─ images/
```

If the repository already has an existing layout/CSS structure, integrate with it instead of replacing everything.

Do not break existing portfolio pages.

---

## 5. `_config.yml` requirements

Add or update `_config.yml` carefully.

Minimum recommended config:

```yml
title: "Koodinpätkiä / Code Bits"
description: "Short technical notes, fixes, code snippets, Linux/Windows tips, and development experiments by Jan-Erik Labbas."
url: "https://jamps3.github.io"
baseurl: ""
lang: "en-FI"
timezone: "Europe/Helsinki"

permalink: /blog/:year/:month/:day/:title/

markdown: kramdown
highlighter: rouge

kramdown:
  input: GFM
  syntax_highlighter: rouge

excerpt_separator: "<!--more-->"

collections: {}

defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: post
      author: "Jan-Erik Labbas"
      comments: false
```

If the site already has a `_config.yml`, merge these values instead of overwriting unrelated settings.

Do not add unsupported plugins unless necessary.

Optional GitHub Pages-supported plugins, only if the repo already uses a Gemfile or GitHub Pages supports them in the current environment:

```yml
plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
```

If using `jekyll-seo-tag`, add it to the default layout head:

```liquid
{% seo %}
```

If not using the plugin, implement basic meta tags manually.

---

## 6. Front matter format for posts

Every blog post must use YAML front matter.

Standard post template:

```md
---
layout: post
title: "Post Title Here"
date: 2026-05-24 03:00:00 +0300
categories: [linux]
tags: [linux, bash, troubleshooting]
excerpt: "One-sentence summary shown on the blog listing."
---

Write the post here in Markdown.

<!--more-->

Longer content continues here.
```

Filename format:

```txt
_posts/YYYY-MM-DD-kebab-case-title.md
```

Example:

```txt
_posts/2019-09-22-add-4k-60hz-mode-to-linux.md
```

Important:

- Use lowercase tag names where possible.
- Prefer short category lists.
- Use `excerpt` explicitly for important migrated posts.
- Use `<!--more-->` if the excerpt should include more than the first paragraph.

---

## 7. Example migrated post

Create one starter migrated post to prove the system works.

File:

```txt
_posts/2019-09-22-add-4k-60hz-mode-to-linux.md
```

Content:

```md
---
layout: post
title: "Add 4K 60Hz Mode to Linux"
date: 2019-09-22 12:00:00 +0300
categories: [linux]
tags: [linux, xrandr, display, 4k, monitor]
excerpt: "How to manually add a missing 4K 60Hz display mode in Linux using cvt and xrandr."
original_url: "https://koodinpatkia.blogspot.com/2019/09/add-4k-60hz-mode-to-linux.html"
---

Sometimes Linux does not automatically expose every display mode your monitor and GPU can use.
For example, 4K may appear only at 30Hz even when 60Hz should work.

This note shows how to manually add a 3840×2160 60Hz mode using `cvt` and `xrandr`.

<!--more-->

## 1. Create a modeline

```bash
cvt 3840 2160 60
```

Example output:

```bash
# 3840x2160 59.98 Hz (CVT) hsync: 134.18 kHz; pclk: 712.75 MHz
Modeline "3840x2160_60.00" 712.75 3840 4160 4576 5312 2160 2163 2168 2237 -hsync +vsync
```

## 2. Check your display output name

```bash
xrandr
```

Look for the connected display name, for example `HDMI-1` or `DP-1`.

## 3. Add the new mode

```bash
xrandr --newmode "3840x2160_60.00" 712.75 3840 4160 4576 5312 2160 2163 2168 2237 -hsync +vsync
```

## 4. Attach the mode to the output

Replace `HDMI-1` with your actual output name:

```bash
xrandr --addmode HDMI-1 "3840x2160_60.00"
```

## 5. Enable the mode

```bash
xrandr --output HDMI-1 --mode "3840x2160_60.00"
```

## Notes

If the screen goes black, wait a few seconds or switch to a TTY with `Ctrl + Alt + F3`.

{% if page.original_url %}
> Originally published on the old Koodinpätkiä blog: {{ page.original_url }}
{% endif %}
```

---

## 8. Layouts

### 8.1 `_layouts/default.html`

Create a generic site layout if one does not already exist.

Required features:

- UTF-8 charset
- responsive viewport
- title handling
- description meta tag
- link to `assets/css/blog.css`
- optional existing global site CSS
- semantic header/main/footer
- navigation link back to home and blog

Skeleton:

```html
<!doctype html>
<html lang="{{ site.lang | default: 'en' }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% if page.title %}{{ page.title }} · {% endif %}{{ site.title }}</title>
  <meta name="description" content="{{ page.excerpt | default: site.description | strip_html | strip_newlines | escape }}">
  <link rel="stylesheet" href="{{ '/assets/css/blog.css' | relative_url }}">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="{{ '/' | relative_url }}">{{ site.title }}</a>
    <nav class="site-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">Home</a>
      <a href="{{ '/blog.html' | relative_url }}">Blog</a>
      <a href="{{ '/archive.html' | relative_url }}">Archive</a>
      <a href="{{ '/tags.html' | relative_url }}">Tags</a>
    </nav>
  </header>

  <main class="site-main">
    {{ content }}
  </main>

  <footer class="site-footer">
    <p>© {{ site.time | date: '%Y' }} Jan-Erik Labbas.</p>
  </footer>

  <script src="{{ '/assets/js/blog.js' | relative_url }}" defer></script>
</body>
</html>
```

If the existing site already has a layout, reuse it and add only the blog-specific pieces.

### 8.2 `_layouts/post.html`

Create a post layout.

Required features:

- title
- date
- categories/tags
- article content
- optional original Blogger URL
- previous/next post navigation
- back to blog link

Skeleton:

```html
---
layout: default
---

<article class="post">
  <header class="post-header">
    <p class="post-kicker">Koodinpätkiä / Code Bits</p>
    <h1>{{ page.title }}</h1>
    {% include post-meta.html post=page %}
    {% include tag-list.html tags=page.tags %}
  </header>

  <div class="post-content">
    {{ content }}
  </div>

  {% if page.original_url %}
    <aside class="post-original">
      Originally published on the old Blogger version of Koodinpätkiä.
      <a href="{{ page.original_url }}" rel="noopener">View original post</a>.
    </aside>
  {% endif %}

  <nav class="post-nav" aria-label="Post navigation">
    {% if page.previous %}
      <a href="{{ page.previous.url | relative_url }}">← {{ page.previous.title }}</a>
    {% endif %}
    {% if page.next %}
      <a href="{{ page.next.url | relative_url }}">{{ page.next.title }} →</a>
    {% endif %}
  </nav>

  <p class="back-link"><a href="{{ '/blog.html' | relative_url }}">← Back to all posts</a></p>
</article>
```

---

## 9. Includes

### 9.1 `_includes/post-meta.html`

```html
{% assign p = include.post | default: page %}
<p class="post-meta">
  <time datetime="{{ p.date | date_to_xmlschema }}">{{ p.date | date: '%Y-%m-%d' }}</time>
  {% if p.categories and p.categories.size > 0 %}
    <span aria-hidden="true">·</span>
    <span>{{ p.categories | join: ', ' }}</span>
  {% endif %}
</p>
```

### 9.2 `_includes/tag-list.html`

```html
{% if include.tags and include.tags.size > 0 %}
  <ul class="tag-list" aria-label="Tags">
    {% for tag in include.tags %}
      <li><a href="{{ '/tags.html' | relative_url }}#{{ tag | slugify }}">#{{ tag }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
```

### 9.3 `_includes/blog-card.html`

```html
<article class="blog-card" data-tags="{{ post.tags | join: ' ' | escape }}" data-title="{{ post.title | downcase | escape }}">
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  {% include post-meta.html post=post %}
  <p>{{ post.excerpt | strip_html | truncate: 220 }}</p>
  {% include tag-list.html tags=post.tags %}
  <a class="read-more" href="{{ post.url | relative_url }}">Read post →</a>
</article>
```

---

## 10. Blog index page

File:

```txt
blog.html
```

Purpose:

- List all posts newest first.
- Provide search/filter field.
- Provide quick tag/category links.
- Make it easy to browse old technical notes.

Content:

```html
---
layout: default
title: "Blog"
permalink: /blog.html
---

<section class="blog-hero">
  <p class="eyebrow">Koodinpätkiä / Code Bits</p>
  <h1>Technical notes, fixes, snippets and experiments</h1>
  <p>
    A personal archive of useful code bits, Linux and Windows notes, debugging fixes,
    web development snippets, and small discoveries.
  </p>
</section>

<section class="blog-tools" aria-label="Blog tools">
  <label for="blog-search">Search posts</label>
  <input id="blog-search" type="search" placeholder="Search Linux, xrandr, Apache, irssi...">
</section>

<section class="post-list" id="post-list">
  {% for post in site.posts %}
    {% include blog-card.html %}
  {% endfor %}
</section>
```

---

## 11. Archive page

File:

```txt
archive.html
```

Purpose:

- Blogger-like archive by year.
- Helpful for migrated old posts.

Implementation:

```html
---
layout: default
title: "Archive"
permalink: /archive.html
---

<section class="page-header">
  <h1>Archive</h1>
  <p>All posts grouped by year.</p>
</section>

{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}

{% for year in posts_by_year %}
  <section class="archive-year">
    <h2>{{ year.name }}</h2>
    <ul class="archive-list">
      {% for post in year.items %}
        <li>
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y-%m-%d' }}</time>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </li>
      {% endfor %}
    </ul>
  </section>
{% endfor %}
```

---

## 12. Tags page

File:

```txt
tags.html
```

Purpose:

- Show all tags.
- Link to posts under each tag.

Implementation:

```html
---
layout: default
title: "Tags"
permalink: /tags.html
---

<section class="page-header">
  <h1>Tags</h1>
  <p>Browse posts by topic.</p>
</section>

{% assign sorted_tags = site.tags | sort %}

{% for tag in sorted_tags %}
  <section class="tag-section" id="{{ tag[0] | slugify }}">
    <h2>#{{ tag[0] }}</h2>
    <ul>
      {% for post in tag[1] %}
        <li>
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y-%m-%d' }}</time>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </li>
      {% endfor %}
    </ul>
  </section>
{% endfor %}
```

---

## 13. Client-side search/filter

File:

```txt
assets/js/blog.js
```

Keep search simple. No indexing library required.

Behavior:

- On `blog.html`, filter `.blog-card` elements by title, tags, and visible text.
- Case-insensitive.
- If no results, show a small message.
- Do not affect non-blog pages.

Implementation:

```js
(function () {
  const input = document.querySelector('#blog-search');
  const list = document.querySelector('#post-list');
  if (!input || !list) return;

  const cards = Array.from(list.querySelectorAll('.blog-card'));
  const empty = document.createElement('p');
  empty.className = 'empty-search-message';
  empty.textContent = 'No matching posts found.';
  empty.hidden = true;
  list.after(empty);

  input.addEventListener('input', () => {
    const query = input.value.trim().toLowerCase();
    let visibleCount = 0;

    for (const card of cards) {
      const haystack = card.textContent.toLowerCase();
      const visible = !query || haystack.includes(query);
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    }

    empty.hidden = visibleCount !== 0;
  });
})();
```

Optional future enhancement:

- Generate a Liquid-powered `search.json` later if full-site search is needed.
- Do not implement this in the first version unless requested.

---

## 14. CSS direction

File:

```txt
assets/css/blog.css
```

Design direction:

- Developer-focused dark theme.
- Good readability for long technical notes.
- Strong code block styling.
- Subtle neon/cyber accent, but not too flashy.
- Mobile-first responsive layout.
- Compatible with existing portfolio design.

Required styling targets:

```txt
body
.site-header
.site-nav
.site-main
.site-footer
.blog-hero
.blog-tools
.post-list
.blog-card
.tag-list
.post
.post-header
.post-content
.post-content pre
.post-content code
.post-nav
.archive-year
.archive-list
.tag-section
```

Minimum CSS features:

- `max-width` readable content column, around `900px` for pages and `760px` for posts.
- Code blocks horizontally scroll on mobile.
- Inline code visibly distinct.
- Links have clear hover/focus states.
- Use `:focus-visible` for keyboard accessibility.
- Use system fonts unless the existing site already has a font system.

Suggested base palette:

```css
:root {
  --bg: #15171c;
  --surface: #1f232b;
  --surface-strong: #262b35;
  --text: #f4f6fb;
  --muted: #b7bfcc;
  --border: #363d4a;
  --accent: #4ea1ff;
  --accent-strong: #64f4d4;
  --code-bg: #0f1117;
}
```

Do not overwrite unrelated global styles unless necessary.

---

## 15. Copy-code buttons

Add optional copy buttons to code blocks in `assets/js/blog.js`.

Requirements:

- Only enhance `<pre><code>` blocks.
- Button text: `Copy` → `Copied!` → `Copy`.
- Gracefully skip if Clipboard API is unavailable.
- Do not require external JS libraries.

Pseudo-implementation:

```js
(function () {
  if (!navigator.clipboard) return;

  document.querySelectorAll('pre > code').forEach((code) => {
    const pre = code.parentElement;
    const button = document.createElement('button');
    button.className = 'copy-code-button';
    button.type = 'button';
    button.textContent = 'Copy';

    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(code.innerText);
        button.textContent = 'Copied!';
        setTimeout(() => (button.textContent = 'Copy'), 1200);
      } catch {
        button.textContent = 'Failed';
        setTimeout(() => (button.textContent = 'Copy'), 1200);
      }
    });

    pre.classList.add('has-copy-button');
    pre.appendChild(button);
  });
})();
```

---

## 16. Migrating old Blogger content

Do not attempt a full automatic migration in the first implementation unless the user asks.

Start with a small curated migration.

Recommended first posts:

1. `Add 4K 60Hz mode to Linux`
2. `Computer waking up from sleep and you don't know why?`
3. `Passing all parameter arguments to irssi alias`
4. `Linux permissions for www-pub group`
5. `SSH port complete tunneling and forwarding`

Migration rules:

- Preserve technical commands accurately.
- Clean up formatting into Markdown.
- Add `original_url` in front matter when known.
- Keep dates close to the original post dates where possible.
- Do not invent content that was not in the original post.
- Add a short excerpt for each migrated post.

Example migrated front matter:

```md
---
layout: post
title: "Computer Waking Up from Sleep and You Don't Know Why?"
date: 2017-01-01 12:00:00 +0300
categories: [windows]
tags: [windows, powercfg, sleep, troubleshooting]
excerpt: "Find out what woke a Windows computer from sleep using powercfg."
original_url: "https://koodinpatkia.blogspot.com/..."
---
```

---

## 17. Navigation integration

Add a blog link to the existing site navigation.

Suggested label options:

```txt
Blog
Code Bits
Koodinpätkiä
```

Recommended visible label:

```txt
Blog
```

Optional sublabel/hero branding:

```txt
Koodinpätkiä / Code Bits
```

If the existing site has Finnish/English mixed navigation, use:

```txt
Blog / Koodinpätkiä
```

---

## 18. Accessibility requirements

Implement basic accessibility from the start:

- Semantic `<main>`, `<article>`, `<nav>`, `<header>`, `<footer>`.
- Visible focus styles.
- Sufficient color contrast.
- Search input has a `<label>`.
- Tag list has accessible label or clear heading.
- Code blocks remain readable and scrollable on mobile.
- Do not rely on color alone to distinguish important UI elements.

---

## 19. SEO / metadata

Minimum SEO requirements:

- Page titles include post title and site title.
- Meta description uses post excerpt or site description.
- Post pages have proper `<article>` structure.
- Add canonical URLs if easy.
- Add RSS feed later only if supported plugin is already available.

Optional if using `jekyll-seo-tag`:

- Add `{% seo %}` in `<head>`.
- Configure `title`, `description`, `url`, and author/social data in `_config.yml`.

Manual fallback meta tags:

```html
<meta name="description" content="{{ page.excerpt | default: site.description | strip_html | strip_newlines | escape }}">
<link rel="canonical" href="{{ page.url | absolute_url }}">
```

---

## 20. Deployment approach

Preferred first version:

- Use GitHub Pages built-in Jekyll build from the selected publishing branch.
- Do not add a custom GitHub Actions workflow unless the repository already uses one or the default Pages build is insufficient.

If the repo already uses GitHub Actions for Pages, add/adjust workflow carefully.

Do not introduce a Node/Vite/Astro/Hugo build pipeline for this blog.

---

## 21. Local preview instructions

Add a short `README` section, not mandatory for implementation.

Recommended options:

### Option A: GitHub-only workflow

```txt
Edit Markdown → commit → push → check GitHub Pages build result
```

### Option B: WSL/Ruby workflow

```bash
bundle install
bundle exec jekyll serve
```

Then open:

```txt
http://localhost:4000
```

### Option C: Docker workflow

Add later only if requested.

---

## 22. Acceptance criteria

Implementation is complete when:

- `blog.html` lists all posts from `_posts/` automatically.
- A new `.md` file in `_posts/` appears automatically after build.
- At least one example post renders correctly.
- Post pages use the `post` layout.
- Tags appear on post cards and post pages.
- `archive.html` groups posts by year.
- `tags.html` groups posts by tag.
- Code blocks render clearly and scroll horizontally on mobile.
- Copy-code buttons work where supported.
- Search field filters the blog list client-side.
- Existing non-blog site pages still work.
- GitHub Pages build succeeds without unsupported plugins.

---

## 23. First implementation task list for Codex

1. Inspect current repository structure.
2. Detect whether a Jekyll `_config.yml` already exists.
3. Detect existing layouts/CSS and avoid breaking them.
4. Add/merge `_config.yml` settings.
5. Add `_layouts/post.html`.
6. Add missing `_layouts/default.html` only if no suitable existing layout exists.
7. Add `_includes/post-meta.html`.
8. Add `_includes/tag-list.html`.
9. Add `_includes/blog-card.html`.
10. Add `blog.html`.
11. Add `archive.html`.
12. Add `tags.html`.
13. Add `assets/css/blog.css` or merge carefully into existing CSS.
14. Add `assets/js/blog.js` with search and copy-code behavior.
15. Add `_posts/2019-09-22-add-4k-60hz-mode-to-linux.md` as a starter migrated post.
16. Add `_drafts/example-draft.md` as a template, if desired.
17. Add navigation link to blog from existing site navigation.
18. Test generated paths and relative URLs.
19. Confirm GitHub Pages compatibility.
20. Summarize changed files and how to add a new post.

---

## 24. Do-not-do list

Do not:

- Build a custom JSON post index for the first version.
- Add a database.
- Add a CMS.
- Add unsupported Jekyll plugins.
- Replace the whole site design unnecessarily.
- Break existing pages.
- Require local Ruby just to publish posts.
- Add complicated pagination in the first version.
- Implement tag pages as generated plugin pages.
- Use external JavaScript libraries for simple filtering.

---

## 25. Future enhancements

After the first version works, possible improvements:

- RSS feed.
- Sitemap.
- Better generated search index.
- Syntax theme matching GitHub dark mode.
- Category landing pages.
- Old Blogger import/migration batch.
- “Updated at” front matter field.
- Series support for related posts.
- Finnish/English language filter.
- Small “copy command” buttons for individual shell command blocks.
- Link previews for posts on the main portfolio page.

---

## 26. Final note for Codex

Prioritize reliability and maintainability over cleverness.

The user specifically likes the `.md` workflow and wants to avoid forgetting manual index entries. Therefore, the core value of this implementation is:

```txt
_posts/*.md → automatic blog
```

Keep the implementation transparent, easy to edit, and compatible with GitHub Pages.
