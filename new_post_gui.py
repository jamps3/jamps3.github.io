#!/usr/bin/env python3
"""
new_post_gui.py - A GUI tool to create new Jekyll posts with prompted metadata.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os
import re

def slugify(title):
    """Convert title to URL-friendly slug."""
    # Convert to lowercase
    slug = title.lower()
    # Replace non-alphanumeric characters (except spaces) with hyphens
    slug = re.sub(r'[^a-z0-9\s]', '', slug)
    # Replace spaces with hyphens
    slug = re.sub(r'\s+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug

def create_post():
    """Handle the create post button click."""
    # Get values from form
    title = title_entry.get().strip()
    if not title:
        messagebox.showerror("Error", "Post title is required!")
        return
    
    categories = categories_entry.get().strip()
    tags = tags_entry.get().strip()
    excerpt = excerpt_entry.get("1.0", tk.END).strip()
    original_url = original_url_entry.get().strip()
    lang = lang_entry.get().strip() or "en"
    migrated = migrated_var.get()
    content = content_entry.get("1.0", tk.END).strip()
    
    # Validation: if migrated, original URL is required
    if migrated and not original_url:
        messagebox.showerror("Error", "Original URL is required for migrated posts!")
        return
    
    # Generate slug and filename
    slug = slugify(title)
    if not slug:
        messagebox.showerror("Error", "Unable to generate slug from title!")
        return
    
    now = datetime.now()
    date_for_filename = now.strftime("%Y-%m-%d")
    date_for_field = now.strftime("%Y-%m-%d %H:%M:%S") + " +03:00"
    
    filename = f"{date_for_filename}-{slug}.md"
    filepath = os.path.join("_posts", filename)
    
    # Check if file already exists
    if os.path.exists(filepath):
        if not messagebox.askyesno("File Exists", 
                                  f"The file {filename} already exists. Overwrite?"):
            return
    
    # Build front matter
    lines = [
        "---",
        "layout: post",
        f"title: \"{title}\"",
        f"date: {date_for_field}",
        f"updated: {date_for_field}",
    ]
    
    # Categories
    if categories:
        # Split by comma, strip whitespace, filter empty
        categories_list = [c.strip() for c in categories.split(",") if c.strip()]
        if categories_list:
            # Quote each category
            quoted_cats = [f'"{cat}"' for cat in categories_list]
            lines.append(f"categories: [{', '.join(quoted_cats)}]")
        else:
            lines.append("categories: []")
    else:
        lines.append("categories: []")
    
    # Tags
    if tags:
        # Split by comma, strip whitespace, filter empty
        tags_list = [t.strip() for t in tags.split(",") if t.strip()]
        if tags_list:
            # Quote each tag
            quoted_tags = [f'"{tag}"' for tag in tags_list]
            lines.append(f"tags: [{', '.join(quoted_tags)}]")
        else:
            lines.append("tags: []")
    else:
        lines.append("tags: []")
    
    # Excerpt
    lines.append(f'excerpt: "{excerpt}"')
    
    # Original URL (only if provided)
    if original_url:
        lines.append(f"original_url: \"{original_url}\"")
    
    # Language
    lines.append(f'lang: "{lang}"')
    
    # Migrated
    lines.append(f"migrated: {str(migrated).lower()}")
    
    lines.append("---")
    
    # Add content if provided
    if content:
        lines.append("")
        lines.append(content)
    
    # Write file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        messagebox.showinfo("Success", f"Post created: {filepath}")
        # Clear form for next post
        title_entry.delete(0, tk.END)
        categories_entry.delete(0, tk.END)
        tags_entry.delete(0, tk.END)
        excerpt_entry.delete("1.0", tk.END)
        original_url_entry.delete(0, tk.END)
        lang_entry.delete(0, tk.END)
        lang_entry.insert(0, "en")
        migrated_var.set(False)  # Reset to unchecked by default
        content_entry.delete("1.0", tk.END)
        title_entry.focus()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create post: {str(e)}")

# Create main window
root = tk.Tk()
root.title("New Jekyll Post Creator")
root.geometry("1000x800")
root.resizable(True, True)

# Create main frame with padding
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Title
ttk.Label(main_frame, text="Post Title *:").grid(row=0, column=0, sticky=tk.W, pady=5)
title_entry = ttk.Entry(main_frame, width=50)
title_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
title_entry.focus()

# Categories
ttk.Label(main_frame, text="Categories (comma-separated):").grid(row=1, column=0, sticky=tk.W, pady=5)
categories_entry = ttk.Entry(main_frame, width=50)
categories_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

# Tags
ttk.Label(main_frame, text="Tags (comma-separated):").grid(row=2, column=0, sticky=tk.W, pady=5)
tags_entry = ttk.Entry(main_frame, width=50)
tags_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

# Excerpt
ttk.Label(main_frame, text="Excerpt:").grid(row=3, column=0, sticky=tk.W, pady=5)
excerpt_frame = ttk.Frame(main_frame)
excerpt_frame.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
excerpt_frame.columnconfigure(0, weight=1)
excerpt_entry = tk.Text(excerpt_frame, width=40, height=4)
excerpt_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
excerpt_scroll = ttk.Scrollbar(excerpt_frame, orient=tk.VERTICAL, command=excerpt_entry.yview)
excerpt_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
excerpt_entry.configure(yscrollcommand=excerpt_scroll.set)

# Original URL
ttk.Label(main_frame, text="Original URL (if migrated):").grid(row=4, column=0, sticky=tk.W, pady=5)
original_url_entry = ttk.Entry(main_frame, width=50)
original_url_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)

# Language
ttk.Button(main_frame, text="EN", width=3, command=lambda: lang_entry.delete(0, tk.END) or lang_entry.insert(0, "en")).grid(row=5, column=2, sticky=tk.W, padx=(5, 0), pady=5)
ttk.Button(main_frame, text="FI", width=3, command=lambda: lang_entry.delete(0, tk.END) or lang_entry.insert(0, "fi")).grid(row=5, column=3, sticky=tk.W, padx=(5, 0), pady=5)
ttk.Label(main_frame, text="Language Code:").grid(row=5, column=0, sticky=tk.W, pady=5)
lang_entry = ttk.Entry(main_frame, width=10)
lang_entry.grid(row=5, column=1, sticky=tk.W, pady=5)
lang_entry.insert(0, "en")

# Migrated
migrated_var = tk.BooleanVar(value=False)  # Default to unchecked
ttk.Checkbutton(main_frame, text="Is this post migrated?", variable=migrated_var).grid(
    row=6, column=0, columnspan=2, sticky=tk.W, pady=10
)

# Content
ttk.Label(main_frame, text="Post Content:").grid(row=7, column=0, sticky=tk.W, pady=5)
content_frame = ttk.Frame(main_frame)
content_frame.grid(row=7, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
content_frame.columnconfigure(0, weight=1)
content_frame.rowconfigure(0, weight=1)
content_entry = tk.Text(content_frame, width=75, height=25)
content_entry.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
content_scroll = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=content_entry.yview)
content_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
content_entry.configure(yscrollcommand=content_scroll.set)

# Buttons frame
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=8, column=0, columnspan=2, pady=20)

# Create Post Button
create_btn = ttk.Button(button_frame, text="Create Post", command=create_post)
create_btn.pack(side=tk.LEFT, padx=5)

# Clear Button
clear_btn = ttk.Button(button_frame, text="Clear Form", 
                      command=lambda: [title_entry.delete(0, tk.END),
                                     categories_entry.delete(0, tk.END),
                                     tags_entry.delete(0, tk.END),
                                     excerpt_entry.delete("1.0", tk.END),
                                     original_url_entry.delete(0, tk.END),
                                     lang_entry.delete(0, tk.END),
                                     lang_entry.insert(0, "en"),
                                     migrated_var.set(False),
                                     content_entry.delete("1.0", tk.END),
                                     title_entry.focus()])
clear_btn.pack(side=tk.LEFT, padx=5)

# Exit Button
exit_btn = ttk.Button(button_frame, text="Exit", command=root.quit)
exit_btn.pack(side=tk.LEFT, padx=5)

# Info label
info_label = ttk.Label(main_frame, 
                      text="* Required fields\nDate and time will be auto-filled\nFilename generated from title\nMigrated posts require Original URL",
                      foreground="gray")
info_label.grid(row=9, column=0, columnspan=2, pady=10)

# Start the GUI
root.mainloop()