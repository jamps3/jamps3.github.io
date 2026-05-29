#!/usr/bin/env python3
"""
loki.py - A GUI tool to create new Jekyll posts with prompted metadata.
"""

import sys
import re
import shutil
from datetime import datetime
import os

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton,
    QComboBox, QCheckBox, QMessageBox, QHBoxLayout, QGridLayout,
    QPlainTextEdit, QFileDialog, QTabWidget, QTextBrowser, QVBoxLayout
)
from PyQt6.QtGui import QTextCursor, QFont
from PyQt6.QtCore import QUrl


def slugify(title):
    """Convert title to URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = slug.strip('-')
    return slug


def get_posts():
    """Get list of existing posts from _posts directory."""
    posts_dir = "_posts"
    if not os.path.exists(posts_dir):
        return []

    posts = []
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            if len(filename) > 11 and filename[4] == '-' and filename[7] == '-':
                date_part = filename[:10]
                slug_part = filename[11:-3]
                posts.append({
                    'filename': filename,
                    'date': date_part,
                    'slug': slug_part,
                    'display': f"{date_part} - {slug_part}"
                })

    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts


def parse_post(filepath):
    """Parse an existing post file and return front matter and content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                post_content = parts[2].strip()
            else:
                front_matter = ""
                post_content = content
        else:
            front_matter = ""
            post_content = content

        front_matter_data = {}
        if front_matter:
            lines = front_matter.strip().split('\n')
            for line in lines:
                line = line.strip()
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()

                    if value.startswith('"') and value.endswith('"') and len(value) >= 2:
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'") and len(value) >= 2:
                        value = value[1:-1]

                    if value.startswith('[') and value.endswith(']'):
                        array_content = value[1:-1].strip()
                        if array_content:
                            items = []
                            for item in array_content.split(','):
                                item = item.strip()
                                if item.startswith('"') and item.endswith('"') and len(item) >= 2:
                                    item = item[1:-1]
                                elif item.startswith("'") and item.endswith("'") and len(item) >= 2:
                                    item = item[1:-1]
                                items.append(item)
                            front_matter_data[key] = items
                        else:
                            front_matter_data[key] = []
                    else:
                        front_matter_data[key] = value

        return front_matter_data, post_content
    except Exception as e:
        return {}, f"Failed to parse post: {str(e)}"


def markdown_to_html(md_text):
    """Convert basic markdown to HTML for preview."""
    html = md_text

    # Escape HTML entities first
    html = html.replace("&", "&")
    html = html.replace("<", "<")
    html = html.replace(">", ">")

    # Code blocks (fenced) - must be done before other inline formatting
    html = re.sub(
        r'```(\w*)\n(.*?)```',
        r'<pre><code>\2</code></pre>',
        html,
        flags=re.DOTALL
    )

    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Images
    html = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        r'<img src="\2" alt="\1" style="max-width:100%;height:auto;">',
        html
    )

    # Links
    html = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'<a href="\2">\1</a>',
        html
    )

    # Headings
    html = re.sub(r'^###### (.+)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html)
    html = re.sub(r'\*(.+?)\*', r'<i>\1</i>', html)

    # Horizontal rules
    html = re.sub(r'^---+\s*$', '<hr>', html, flags=re.MULTILINE)

    # Unordered lists (simple)
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>)\n?', r'<ul>\1</ul>', html)

    # Line breaks (double newline = paragraph, single newline = <br>)
    paragraphs = re.split(r'\n\s*\n', html)
    processed = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if para.startswith('<h') or para.startswith('<pre') or para.startswith('<ul') or para.startswith('<hr'):
            processed.append(para)
        else:
            para_br = para.replace('\n', '<br>')
            processed.append(f'<p>{para_br}</p>')
    html = '\n'.join(processed)

    return html


class PostCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.current_post_file = None
        self.posts_list = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("New Jekyll Post Creator")
        self.resize(1200, 900)

        main_layout = QGridLayout()
        self.setLayout(main_layout)

        # Row 0 - Title
        main_layout.addWidget(QLabel("Post Title *:"), 0, 0)
        self.title_entry = QLineEdit()
        main_layout.addWidget(self.title_entry, 0, 1)

        # Row 1 - Categories
        main_layout.addWidget(QLabel("Categories (comma-separated):"), 1, 0)
        self.categories_entry = QLineEdit()
        main_layout.addWidget(self.categories_entry, 1, 1)

        # Row 2 - Tags
        main_layout.addWidget(QLabel("Tags (comma-separated):"), 2, 0)
        self.tags_entry = QLineEdit()
        main_layout.addWidget(self.tags_entry, 2, 1)

        # Row 3 - Excerpt
        main_layout.addWidget(QLabel("Excerpt:"), 3, 0)
        self.excerpt_entry = QTextEdit()
        self.excerpt_entry.setMaximumHeight(60)
        main_layout.addWidget(self.excerpt_entry, 3, 1)

        # Row 4 - Original URL
        main_layout.addWidget(QLabel("Original URL (if migrated):"), 4, 0)
        self.original_url_entry = QLineEdit()
        main_layout.addWidget(self.original_url_entry, 4, 1)

        # Row 5 - Language
        main_layout.addWidget(QLabel("Language Code:"), 5, 0)
        lang_hbox = QHBoxLayout()
        self.lang_entry = QLineEdit()
        self.lang_entry.setMaximumWidth(100)
        self.lang_entry.setText("en")
        en_btn = QPushButton("EN")
        en_btn.clicked.connect(lambda: self.lang_entry.setText("en"))
        fi_btn = QPushButton("FI")
        fi_btn.clicked.connect(lambda: self.lang_entry.setText("fi"))
        lang_hbox.addWidget(self.lang_entry)
        lang_hbox.addWidget(en_btn)
        lang_hbox.addWidget(fi_btn)
        lang_hbox.addStretch()
        main_layout.addLayout(lang_hbox, 5, 1)

        # Row 6 - Migrated checkbox
        self.migrated_var = False
        self.migrated_cb = QCheckBox("Is this post migrated?")
        main_layout.addWidget(self.migrated_cb, 6, 0, 1, 2)

        # Row 7 - Edit Existing Post
        main_layout.addWidget(QLabel("Edit Existing Post:"), 7, 0)
        post_hbox = QHBoxLayout()
        self.post_combo = QComboBox()
        self.post_combo.setEditable(False)
        self.post_combo.setMinimumWidth(600)
        load_posts_btn = QPushButton("Load Posts")
        load_posts_btn.clicked.connect(self.refresh_post_list)
        load_post_btn = QPushButton("Load Post")
        load_post_btn.clicked.connect(self.load_post)
        post_hbox.addWidget(self.post_combo)
        post_hbox.addWidget(load_posts_btn)
        post_hbox.addWidget(load_post_btn)
        post_hbox.addStretch()
        main_layout.addLayout(post_hbox, 7, 1)

        # Row 8 - Insert Code Block
        code_hbox = QHBoxLayout()
        main_layout.addWidget(QLabel("Insert Code Block:"), 8, 0)
        self.language_combo = QComboBox()
        languages = [
            "Text", "Python", "JavaScript", "Bash", "JSON", "HTML", "CSS", "XML",
            "YAML", "SQL", "C", "C++", "Java", "Kotlin", "Rust", "Go", "PHP",
            "Diff", "INI", "TOML", "Markdown"
        ]
        self.language_combo.addItems(languages)
        self.language_combo.setCurrentText("Python")
        add_code_btn = QPushButton("Add")
        add_code_btn.clicked.connect(self.insert_code_block)
        code_hbox.addWidget(self.language_combo)
        code_hbox.addWidget(add_code_btn)
        code_hbox.addStretch()
        main_layout.addLayout(code_hbox, 8, 1)

        # Row 9 - Upload Image
        img_hbox = QHBoxLayout()
        main_layout.addWidget(QLabel("Upload Image:"), 9, 0)
        self.img_path_entry = QLineEdit()
        self.img_path_entry.setReadOnly(True)
        self.img_path_entry.setPlaceholderText("Select an image file...")
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_image)
        upload_img_btn = QPushButton("Insert Image")
        upload_img_btn.clicked.connect(self.upload_image)
        img_hbox.addWidget(self.img_path_entry)
        img_hbox.addWidget(browse_btn)
        img_hbox.addWidget(upload_img_btn)
        img_hbox.addStretch()
        main_layout.addLayout(img_hbox, 9, 1)

        # Row 10 - Post Content (TabWidget with Edit/Preview, takes all remaining space)
        main_layout.addWidget(QLabel("Post Content:"), 10, 0)
        content_container = QWidget()
        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)

        self.content_tabs = QTabWidget()
        self.content_tabs.setTabPosition(QTabWidget.TabPosition.North)

        self.content_entry = QTextEdit()
        self.content_entry.textChanged.connect(self.update_preview)
        self.content_tabs.addTab(self.content_entry, "Edit")

        self.preview_browser = QTextBrowser()
        self.preview_browser.setOpenExternalLinks(True)
        self.content_tabs.addTab(self.preview_browser, "Preview")

        content_layout.addWidget(self.content_tabs)
        main_layout.addWidget(content_container, 10, 1)

        # Set column stretch: column 1 gets all extra horizontal space
        main_layout.setColumnStretch(0, 0)
        main_layout.setColumnStretch(1, 1)

        # Set row stretch: row 10 (Post Content) gets all extra vertical space
        for r in range(11):
            main_layout.setRowStretch(r, 0)
        main_layout.setRowStretch(10, 1)

        # Row 11 - Buttons
        btn_hbox = QHBoxLayout()
        create_btn = QPushButton("Create Post")
        create_btn.clicked.connect(self.create_post)
        clear_btn = QPushButton("Clear Form")
        clear_btn.clicked.connect(self.clear_form)
        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close)
        btn_hbox.addWidget(create_btn)
        btn_hbox.addWidget(clear_btn)
        btn_hbox.addWidget(exit_btn)
        btn_hbox.addStretch()
        main_layout.addLayout(btn_hbox, 11, 1)

        # Row 12 - Info label
        info_label = QLabel(
            "* Required fields | Date and time auto-filled | Migrated posts require Original URL | Images copied to _images/"
        )
        info_label.setStyleSheet("color: gray;")
        main_layout.addWidget(info_label, 12, 0, 1, 2)

        # Row 13 - Log area
        main_layout.addWidget(QLabel("Log:"), 13, 0)
        self.log_area = QPlainTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setMaximumHeight(80)
        log_font = QFont("Consolas", 9)
        self.log_area.setFont(log_font)
        main_layout.addWidget(self.log_area, 13, 1)

        self.title_entry.setFocus()

    def log_message(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        if level == "ERROR":
            prefix = "ERROR"
        elif level == "WARNING":
            prefix = "WARN"
        else:
            prefix = "INFO"
        self.log_area.appendPlainText(f"[{timestamp}] {prefix}: {message}")

    def update_preview(self):
        md_text = self.content_entry.toPlainText()
        html = markdown_to_html(md_text)
        base_url = QUrl.fromLocalFile(os.getcwd() + os.sep)
        self.preview_browser.document().setBaseUrl(base_url)
        self.preview_browser.setHtml(html)

    def browse_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "",
            "Images (*.png *.jpg *.jpeg *.gif *.svg *.webp *.bmp *.ico)"
        )
        if file_path:
            self.img_path_entry.setText(file_path)

    def upload_image(self):
        file_path = self.img_path_entry.text()
        if not file_path:
            self.log_message("No image selected! Browse for an image first.", "WARNING")
            return

        if not os.path.isfile(file_path):
            self.log_message("Selected file does not exist!", "ERROR")
            return

        img_dir = "_images"
        os.makedirs(img_dir, exist_ok=True)

        filename = os.path.basename(file_path)

        dest_path = os.path.join(img_dir, filename)
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(dest_path):
            dest_path = os.path.join(img_dir, f"{base}_{counter}{ext}")
            counter += 1

        try:
            shutil.copy2(file_path, dest_path)
            rel_path = f"_images/{os.path.basename(dest_path)}"

            cursor = self.content_entry.textCursor()
            alt_text = os.path.splitext(filename)[0].replace("-", " ").replace("_", " ")
            img_markdown = f"![{alt_text}]({rel_path})"
            cursor.insertText(img_markdown)
            self.content_entry.setTextCursor(cursor)

            self.log_message(f"Image inserted: {rel_path}")
            self.img_path_entry.clear()
        except Exception as e:
            self.log_message(f"Failed to copy image: {str(e)}", "ERROR")

    def refresh_post_list(self):
        self.posts_list = get_posts()
        self.post_combo.clear()
        for post in self.posts_list:
            self.post_combo.addItem(post['display'])
        if self.posts_list:
            self.post_combo.setCurrentIndex(0)
            self.log_message(f"Loaded {len(self.posts_list)} posts from _posts directory")
        else:
            self.log_message("No posts found in _posts directory", "WARNING")

    def insert_code_block(self):
        language = self.language_combo.currentText()
        if not language:
            self.log_message("Please select a language!", "WARNING")
            return

        code_block = f"```{language}\n\n```"
        cursor = self.content_entry.textCursor()
        cursor.insertText(code_block)

        cursor.movePosition(QTextCursor.MoveOperation.Up)
        cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)
        self.content_entry.setTextCursor(cursor)

    def load_post(self):
        selection = self.post_combo.currentText()
        if not selection:
            self.log_message("Please select a post!", "WARNING")
            return

        selected_post = None
        for post in self.posts_list:
            if post['display'] == selection:
                selected_post = post
                break

        if not selected_post:
            self.log_message("Post not found!", "ERROR")
            return

        filepath = os.path.join("_posts", selected_post['filename'])
        front_matter, content = parse_post(filepath)
        if isinstance(content, str) and content.startswith("Failed to parse"):
            self.log_message(content, "ERROR")
            return

        self.title_entry.setText(front_matter.get('title', ''))
        categories = front_matter.get('categories', [])
        if isinstance(categories, list):
            self.categories_entry.setText(', '.join(categories))
        else:
            self.categories_entry.setText(str(categories))

        tags = front_matter.get('tags', [])
        if isinstance(tags, list):
            self.tags_entry.setText(', '.join(tags))
        else:
            self.tags_entry.setText(str(tags))

        self.excerpt_entry.setPlainText(front_matter.get('excerpt', ''))
        self.original_url_entry.setText(front_matter.get('original_url', ''))
        self.lang_entry.setText(front_matter.get('lang', 'en'))

        migrated_val = front_matter.get('migrated', False)
        if isinstance(migrated_val, str):
            self.migrated_cb.setChecked(migrated_val.lower() in ['true', 'yes', '1'])
        else:
            self.migrated_cb.setChecked(bool(migrated_val))

        self.content_entry.setPlainText(content)
        self.current_post_file = filepath

        self.log_message(f"Loaded post: {selected_post['filename']}")

    def create_post(self):
        title = self.title_entry.text().strip()
        if not title:
            self.log_message("Post title is required!", "ERROR")
            return

        categories = self.categories_entry.text().strip()
        tags = self.tags_entry.text().strip()
        excerpt = self.excerpt_entry.toPlainText().strip()
        original_url = self.original_url_entry.text().strip()
        lang = self.lang_entry.text().strip() or "en"
        migrated = self.migrated_cb.isChecked()
        content = self.content_entry.toPlainText().strip()

        if migrated and not original_url:
            self.log_message("Original URL is required for migrated posts!", "ERROR")
            return

        slug = slugify(title)
        if not slug:
            self.log_message("Unable to generate slug from title!", "ERROR")
            return

        now = datetime.now()
        date_for_filename = now.strftime("%Y-%m-%d")
        date_for_field = now.strftime("%Y-%m-%d %H:%M:%S") + " +03:00"

        if self.current_post_file:
            filename = os.path.basename(self.current_post_file)
            if len(filename) >= 10 and filename[4] == '-' and filename[7] == '-':
                date_for_filename = filename[:10]
                try:
                    with open(self.current_post_file, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    if file_content.startswith('---'):
                        parts = file_content.split('---', 2)
                        if len(parts) >= 3:
                            front_matter = parts[1]
                            date_match = re.search(r'date:\s*"?(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})', front_matter)
                            if date_match:
                                date_for_field = date_match.group(1) + " +03:00"
                except:
                    pass

        filename = f"{date_for_filename}-{slug}.md"
        filepath = os.path.join("_posts", filename)

        if os.path.exists(filepath) and not self.current_post_file:
            if not QMessageBox.question(self, "File Exists",
                                      f"The file {filename} already exists. Overwrite?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
                return

        lines = [
            "---",
            "layout: post",
            f"title: \"{title}\"",
            f"date: {date_for_field}",
            f"updated: {date_for_field}",
        ]

        if categories:
            categories_list = [c.strip() for c in categories.split(",") if c.strip()]
            if categories_list:
                quoted_cats = [f'"{cat}"' for cat in categories_list]
                lines.append(f"categories: [{', '.join(quoted_cats)}]")
            else:
                lines.append("categories: []")
        else:
            lines.append("categories: []")

        if tags:
            tags_list = [t.strip() for t in tags.split(",") if t.strip()]
            if tags_list:
                quoted_tags = [f'"{tag}"' for tag in tags_list]
                lines.append(f"tags: [{', '.join(quoted_tags)}]")
            else:
                lines.append("tags: []")
        else:
            lines.append("tags: []")

        lines.append(f'excerpt: "{excerpt}"')

        if original_url:
            lines.append(f"original_url: \"{original_url}\"")

        lines.append(f'lang: "{lang}"')
        lines.append(f"migrated: {str(migrated).lower()}")
        lines.append("---")

        if content:
            lines.append("")
            lines.append(content)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            self.log_message(f"Post saved: {filepath}")
            self.clear_form()
            self.current_post_file = None
        except Exception as e:
            self.log_message(f"Failed to create post: {str(e)}", "ERROR")

    def clear_form(self):
        self.title_entry.clear()
        self.categories_entry.clear()
        self.tags_entry.clear()
        self.excerpt_entry.clear()
        self.original_url_entry.clear()
        self.lang_entry.setText("en")
        self.migrated_cb.setChecked(False)
        self.content_entry.clear()
        self.title_entry.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostCreator()
    window.show()
    sys.exit(app.exec())