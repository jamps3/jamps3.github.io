# jamps3.github.io

Source repository for my personal GitHub Pages website.

🌐 Live site: [https://jamps3.github.io](https://jamps3.github.io)

---

## Main Pages

| Page                                                                  | Description                                                       |
| --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [CV (English)](https://jamps3.github.io/)                             | Main CV and professional profile                                  |
| [CV (Finnish)](https://jamps3.github.io/index-fi.html)                | Finnish version of the CV                                         |
| [Portfolio](https://jamps3.github.io/portfolio.html)                  | Software, electronics, and web development projects               |
| [Blog — Koodinpätkiä / Code Bits](https://jamps3.github.io/blog.html) | Technical notes, snippets, troubleshooting, and development posts |
| [Archive](https://jamps3.github.io/archive.html)                      | Blog archive                                                      |
| [Tags](https://jamps3.github.io/tags.html)                            | Blog tag listing                                                  |

---

## About This Repository

This repository contains the source files for my GitHub Pages website, including:

* Personal CV pages
* Project portfolio
* Jekyll-based technical blog
* Static assets and screenshots
* Custom layouts and includes
* Helper scripts and tooling
* Migrated Blogger posts

The site combines software development, Linux, electronics, automation, accessibility, and practical ICT topics.

---

## Repository Structure

```txt
.
├── _drafts/         # Draft blog posts
├── _includes/       # Shared Jekyll include files
├── _layouts/        # Jekyll page layouts
├── _posts/          # Blog posts
├── assets/          # CSS, JS, fonts, and other assets
├── img/             # Images and screenshots
├── scripts/         # Utility scripts
├── blog.html        # Blog index
├── portfolio.html   # Portfolio page
├── index.html       # English CV
├── index-fi.html    # Finnish CV
├── archive.html     # Blog archive
├── tags.html        # Blog tags
└── search.json      # Blog search index
```

---

## Featured Projects

### Desktop / Python

* [Quantifile](https://github.com/jamps3/Quantifile)
  Disk space visualization and treemap analysis tool.

* Cross-platform 3D File Manager
  Experimental spiral-based visual file navigation concept using Qt3D.

* Customer Order Database UI
  PyQt6 + MariaDB + AWS desktop application project.

* SVG Multi-mode Clock
  Experimental SVG clock with multiple time systems and visual modes.

* LeetIRCPythonBot
  Modular Python IRC bot with automation and API integrations.

---

### Android / Kotlin

* PetzyTop
  Android overlay companion / virtual pet experiments.

* Loitsio
  Gamified productivity and life-management application concepts.

* Soumari
  Privacy-first audio recorder concept.

* KuvaTaru
  Visual support / routine-building application concept.

---

### Web / CMS / Infrastructure

* WordPress and ProcessWire website development
* Linux server administration and automation
* SEO and structured data experiments
* Accessibility and usability improvements
* Static site customization and scripting

---

## Blog Workflow

This repository includes a lightweight Jekyll blog for short technical notes, fixes, commands, snippets, experiments, and migrated Blogger posts.

### Creating a Post

Create a file in `_posts/` using:

```txt
YYYY-MM-DD-post-title.md
```

Example:

```txt
2026-05-24-linux-troubleshooting.md
```

---

### Example Front Matter

```md
---
layout: post
title: "Post Title"
date: 2026-05-24 03:00:00 +0300
categories: [linux]
tags: [linux, bash, troubleshooting]
excerpt: "One-sentence summary shown on the blog listing."
---
```

---

## Local Development

Local preview is optional. WSL is usually the easiest Ruby/Jekyll environment on Windows.

### Install dependencies

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
gem install bundler
bundle config set --local path '.bundle'
bundle install
```

### Make sure bundle is in PATH:
```bash
echo 'export PATH="$HOME/.local/share/gem/ruby/3.3.0/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Start local server

```bash
bundle exec jekyll serve --livereload
```

Then open:

```txt
http://localhost:4000
```

---

## Technologies Used

* Jekyll
* GitHub Pages
* HTML
* CSS
* JavaScript
* Markdown
* Python
* Liquid templates

---

## Notes

This repository acts both as:

1. The source code repository for the public website
2. A lightweight personal knowledge base and technical archive

The blog intentionally contains practical troubleshooting notes, quick fixes, commands, experiments, and development-related documentation.

---

## Contact

* GitHub: [https://github.com/jamps3](https://github.com/jamps3)
* LinkedIn: [https://www.linkedin.com/in/jan-erik-labbas-2a5398b6/](https://www.linkedin.com/in/jan-erik-labbas-2a5398b6/)
* Email: mailto:jamps3@gmail.com
