$ErrorActionPreference = "Stop"

$feedUrl = "https://koodinpatkia.blogspot.com/feeds/posts/default?alt=json&max-results=500"
$root = Split-Path -Parent $PSScriptRoot
$postsDir = Join-Path $root "_posts"

New-Item -ItemType Directory -Force -Path $postsDir | Out-Null

function ConvertTo-Slug {
  param([string] $Text)

  $decoded = [System.Net.WebUtility]::HtmlDecode($Text).ToLowerInvariant()
  $normalized = $decoded.Normalize([Text.NormalizationForm]::FormD)
  $builder = [Text.StringBuilder]::new()

  foreach ($char in $normalized.ToCharArray()) {
    $category = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($char)
    if ($category -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
      [void] $builder.Append($char)
    }
  }

  $slug = $builder.ToString()
  $slug = [regex]::Replace($slug, "[^a-z0-9]+", "-").Trim("-")
  if ([string]::IsNullOrWhiteSpace($slug)) {
    return "post"
  }

  return $slug
}

function ConvertTo-YamlString {
  param([string] $Text)

  $clean = [System.Net.WebUtility]::HtmlDecode($Text)
  $clean = $clean -replace "`r", " " -replace "`n", " "
  $clean = $clean -replace "\s+", " "
  return '"' + ($clean.Trim() -replace '\\', '\\' -replace '"', '\"') + '"'
}

function ConvertTo-Excerpt {
  param([string] $Html)

  $text = [regex]::Replace($Html, "<script[\s\S]*?</script>", "", "IgnoreCase")
  $text = [regex]::Replace($text, "<style[\s\S]*?</style>", "", "IgnoreCase")
  $text = [regex]::Replace($text, "<[^>]+>", " ")
  $text = [System.Net.WebUtility]::HtmlDecode($text)
  $text = $text -replace "\s+", " "
  $text = $text.Trim()

  if ($text.Length -gt 180) {
    return $text.Substring(0, 177).TrimEnd() + "..."
  }

  if ([string]::IsNullOrWhiteSpace($text)) {
    return "Migrated post from the old Koodinpätkiä Blogger archive."
  }

  return $text
}

function ConvertTo-TagArray {
  param(
    $Categories,
    [string] $Title,
    [string] $Html
  )

  if ($null -eq $Categories) {
    $inferred = Get-InferredTags $Title $Html
    return "[" + (($inferred | ForEach-Object { '"' + $_ + '"' }) -join ", ") + "]"
  }

  $tags = @()
  foreach ($category in @($Categories)) {
    if ($category.term) {
      $tags += [System.Net.WebUtility]::HtmlDecode([string] $category.term).ToLowerInvariant()
    }
  }

  if ($tags.Count -eq 0) {
    $tags = Get-InferredTags $Title $Html
  }

  $quoted = $tags | Sort-Object -Unique | ForEach-Object {
    '"' + ($_ -replace '\\', '\\' -replace '"', '\"') + '"'
  }

  return "[" + ($quoted -join ", ") + "]"
}

function Get-InferredTags {
  param(
    [string] $Title,
    [string] $Html
  )

  $haystack = (($Title + " " + $Html) -replace "<[^>]+>", " ").ToLowerInvariant()
  $tags = @("blogger-import")

  if ($haystack -match "linux|xrandr|cvt|ssh|apache|debian|/var/www|chmod|chown|rsync|tar") {
    $tags += "linux"
  }
  if ($haystack -match "windows|powercfg|gpu|putty") {
    $tags += "windows"
  }
  if ($haystack -match "sharepoint|xsl|ddwrt") {
    $tags += "sharepoint"
  }
  if ($haystack -match "css|html|jquery|firefox|browser") {
    $tags += "web"
  }
  if ($haystack -match "android|wifi|wlan") {
    $tags += "android"
  }

  return $tags | Sort-Object -Unique
}

function Get-PrimaryCategory {
  param(
    $Categories,
    [string] $Title,
    [string] $Html
  )

  $haystack = (($Title + " " + $Html) -replace "<[^>]+>", " ").ToLowerInvariant()

  if ($null -eq $Categories) {
    if ($haystack -match "linux|xrandr|cvt|ssh|apache|debian|/var/www|chmod|chown|rsync|tar") {
      return "linux"
    }
    if ($haystack -match "windows|powercfg|gpu|putty") {
      return "windows"
    }
    if ($haystack -match "sharepoint|xsl|ddwrt") {
      return "sharepoint"
    }
    if ($haystack -match "css|html|jquery|firefox|browser") {
      return "web"
    }
    if ($haystack -match "android|wifi|wlan") {
      return "android"
    }
    return "notes"
  }

  foreach ($category in @($Categories)) {
    if ($category.term) {
      $term = [System.Net.WebUtility]::HtmlDecode([string] $category.term).ToLowerInvariant()
      if ($term -match "linux|ssh|apache|debian|www|permissions") {
        return "linux"
      }
      if ($term -match "sharepoint|xsl|ddwrt") {
        return "sharepoint"
      }
      if ($term -match "css|html|jquery|web|firefox") {
        return "web"
      }
      if ($term -match "android|wifi|wlan") {
        return "android"
      }
    }
  }

  return "notes"
}

$feedContent = Invoke-WebRequest -Uri $feedUrl -UseBasicParsing | Select-Object -ExpandProperty Content
try {
  $feed = $feedContent | ConvertFrom-Json -DateKind String
} catch {
  $feed = $feedContent | ConvertFrom-Json
}
$entries = @($feed.feed.entry)
$written = @()

foreach ($entry in $entries) {
  $title = [System.Net.WebUtility]::HtmlDecode([string] $entry.title.'$t')
  $publishedValue = $entry.published.'$t'
  $updatedValue = $entry.updated.'$t'

  if ($publishedValue -is [datetime]) {
    $published = [DateTimeOffset]::new($publishedValue)
  } else {
    $published = [DateTimeOffset]::Parse([string] $publishedValue, [Globalization.CultureInfo]::InvariantCulture)
  }

  if ($updatedValue -is [datetime]) {
    $updated = [DateTimeOffset]::new($updatedValue)
  } else {
    $updated = [DateTimeOffset]::Parse([string] $updatedValue, [Globalization.CultureInfo]::InvariantCulture)
  }
  $datePrefix = $published.ToString("yyyy-MM-dd")
  $slug = ConvertTo-Slug $title
  $filename = "$datePrefix-$slug.md"
  $path = Join-Path $postsDir $filename

  $originalUrl = ""
  foreach ($link in @($entry.link)) {
    if ($link.rel -eq "alternate" -and $link.type -eq "text/html") {
      $originalUrl = [string] $link.href
      break
    }
  }

  $html = [string] $entry.content.'$t'
  $html = $html -replace 'https://blogger\.googleusercontent\.com/img/b/R29vZ2xl/AVvXsEhIQajuFQlhD0CI7yymI0i5CuLPF2ssDRZHtRdq9o46I2OwKdEEMw5hW5-tQX6QLiGUPGFEMerlS9bENSn0gtJF030KW-zfptXTv1esbLu52c1yO3NOFYzPFXsCHvI9GzwldKJ76qeGAnw/s1600/puttyconfig2\.png', "{{ '/assets/blog/images/puttyconfig2.png' | relative_url }}"
  $html = $html -replace 'https://blogger\.googleusercontent\.com/img/b/R29vZ2xl/AVvXsEjlxlIRUcclJn9pDM1P-piSVJ1i7sDgIum2NO-XufSLxQHmXclEFem_E-d5l3LmjROeXqffiB6eLbuWGkzHf-ikwAqsfpMt_LA4ip-jybYq-j-_jrnj1GpQ_owD4FcZZtl5aCGHNojkZ1o/s1600/puttyconfig1\.png', "{{ '/assets/blog/images/puttyconfig1.png' | relative_url }}"
  $html = $html -replace '<a href="\{\{ ''/assets/blog/images/puttyconfig2\.png'' \| relative_url \}" imageanchor="1"><img border="0" src="\{\{ ''/assets/blog/images/puttyconfig2\.png'' \| relative_url \}" height="397" width="400" /></a>', '<a href="{{ ''/assets/blog/images/puttyconfig2.png'' | relative_url }}"><img src="{{ ''/assets/blog/images/puttyconfig2.png'' | relative_url }}" height="397" width="400" alt="PuTTY configuration screenshot showing SSH tunnel settings." /></a>'
  $html = $html -replace '<a href="\{\{ ''/assets/blog/images/puttyconfig1\.png'' \| relative_url \}" imageanchor="1"><img border="0" src="\{\{ ''/assets/blog/images/puttyconfig1\.png'' \| relative_url \}" height="398" width="400" /></a>', '<a href="{{ ''/assets/blog/images/puttyconfig1.png'' | relative_url }}"><img src="{{ ''/assets/blog/images/puttyconfig1.png'' | relative_url }}" height="398" width="400" alt="PuTTY configuration screenshot showing forwarded port settings." /></a>'
  $excerpt = ConvertTo-Excerpt $html
  $tags = ConvertTo-TagArray $entry.category $title $html
  $category = Get-PrimaryCategory $entry.category $title $html
  $publishedText = $published.ToString("yyyy-MM-dd HH\:mm\:ss zzz", [Globalization.CultureInfo]::InvariantCulture)
  $updatedText = $updated.ToString("yyyy-MM-dd HH\:mm\:ss zzz", [Globalization.CultureInfo]::InvariantCulture)

  $markdown = @"
---
layout: post
title: $(ConvertTo-YamlString $title)
date: $publishedText
updated: $updatedText
categories: [$category]
tags: $tags
excerpt: $(ConvertTo-YamlString $excerpt)
original_url: $(ConvertTo-YamlString $originalUrl)
---

$html
"@

  Set-Content -LiteralPath $path -Value $markdown -Encoding UTF8
  $written += $filename
}

$written | Sort-Object
Write-Host "Migrated $($written.Count) posts."
