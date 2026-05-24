$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$postsDir = Join-Path $root "_posts"

function Decode-Text {
  param([string] $Text)
  return [System.Net.WebUtility]::HtmlDecode($Text).Replace([string][char]13, "")
}

function Convert-CodeBlock {
  param($Match)

  $code = $Match.Groups["code"].Value
  $code = $code -replace '<br\s*/?>', ([string][char]10)
  $code = $code -replace '<[^>]+>', ""
  $code = Decode-Text $code
  $code = $code -replace "(`n){3,}", "`n`n"
  $code = $code.Trim()

  if ([string]::IsNullOrWhiteSpace($code)) {
    return ""
  }

  return ([string][char]10) + ([string][char]10) + '```text' + ([string][char]10) + $code + ([string][char]10) + '```'
}

function Convert-Body {
  param([string] $Body)

  $body = $Body.Replace([string][char]13, "")

  $patterns = @(
    "<pre[^>]*>\s*<code[^>]*>(?<code>[\s\S]*?)</code>\s*</pre>",
    "<code[^>]*>\s*<pre[^>]*>(?<code>[\s\S]*?)</pre>\s*</code>",
    "<pre[^>]*>(?<code>[\s\S]*?)</pre>",
    "<blockquote[^>]*>(?<code>[\s\S]*?)</blockquote>",
    "<code\s+class=`"prettyprint`"[^>]*>(?<code>[\s\S]*?)</code>",
    "<code>(?<code>[\s\S]*?)</code>"
  )

  foreach ($pattern in $patterns) {
    $body = [regex]::Replace($body, $pattern, { param($match) Convert-CodeBlock $match }, "IgnoreCase")
  }

  $body = $body -replace '<br\s*/?>', ([string][char]10)
  $body = $body -replace '<span[^>]*>', ''
  $body = $body -replace '</span>', ''
  $body = $body -replace '<tt>', ''
  $body = $body -replace '</tt>', ''
  $body = $body -replace '<b>', '**'
  $body = $body -replace '</b>', '**'
  $body = $body -replace '<h2[^>]*>', "## "
  $body = $body -replace '</h2>', ([string][char]10 + [string][char]10)
  $body = $body -replace "(?m)^##\s*\n", "## "
  $body = $body -replace '&nbsp;', ' '
  $body = $body -replace '[ \t]+$', ''
  $body = $body -replace "(`n){3,}", ([string][char]10 + [string][char]10)

  return $body.Trim() + ([string][char]10)
}

foreach ($file in Get-ChildItem -LiteralPath $postsDir -Filter "*.md") {
  $content = Get-Content -LiteralPath $file.FullName -Raw
  $match = [regex]::Match($content, '\A---\r?\n(?<front>[\s\S]*?)\r?\n---\r?\n(?<body>[\s\S]*)\z')

  if (-not $match.Success) {
    continue
  }

  $front = $match.Groups["front"].Value.Replace([string][char]13, "")
  $body = $match.Groups["body"].Value

  if ($front -match '(?m)^original_url:' -and $front -notmatch '(?m)^migrated:') {
    $front += "`nmigrated: true"
  }

  if ($front -notmatch '(?m)^lang:') {
    $front += "`nlang: en"
  }

  $cleaned = Convert-Body $body
  $newContent = "---`n$front`n---`n`n$cleaned"
  Set-Content -LiteralPath $file.FullName -Value $newContent -Encoding UTF8
}

Write-Host "Cleaned migrated post formatting."
