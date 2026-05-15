# Создаёт GitHub Issues для BUG-01..BUG-03.
# Требуется: gh auth login (один раз)
# Запуск из корня репозитория: .\scripts\create_github_issues.ps1

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $repoRoot

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "GitHub CLI (gh) не найден. Установите: winget install GitHub.cli"
}

$auth = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Сначала войдите в GitHub: gh auth login" -ForegroundColor Yellow
    exit 1
}

$existing = gh issue list --limit 10 --json number,title 2>$null | ConvertFrom-Json
if ($existing.Count -gt 0) {
    Write-Host "В репозитории уже есть Issues:" -ForegroundColor Yellow
    $existing | ForEach-Object { Write-Host "  #$($_.number) $($_.title)" }
    $answer = Read-Host "Создать BUG-01..03 всё равно? (y/N)"
    if ($answer -notmatch '^[yY]') { exit 0 }
}

function New-BugIssue {
    param(
        [string]$Title,
        [string]$BodyFile
    )
    $body = Get-Content -Path $BodyFile -Raw -Encoding UTF8
    gh issue create --title $Title --body $body
}

Write-Host "Создание Issues..." -ForegroundColor Cyan

$i1 = New-BugIssue -Title "BUG-01: Сервис позволяет перевести 0 ₽" -BodyFile "scripts/issue-bodies/BUG-01.md"
Write-Host "Создан: $i1"

$i2 = New-BugIssue -Title "BUG-02: Сервис позволяет перевести отрицательную сумму" -BodyFile "scripts/issue-bodies/BUG-02.md"
Write-Host "Создан: $i2"

$i3 = New-BugIssue -Title "BUG-03: Перевод в USD суммы, превышающей баланс счёта" -BodyFile "scripts/issue-bodies/BUG-03.md"
Write-Host "Создан: $i3"

Write-Host "`nГотово. Обновите ссылки в README, если номера Issues отличаются от #1–#3." -ForegroundColor Green
