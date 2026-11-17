# Universal Auto-Install Skills Script for PowerShell
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$rootDir = Split-Path -Parent $scriptDir

Write-Host "[Auto-Skills] Running Skill Verification Engine..." -ForegroundColor Cyan

if (Get-Command node -ErrorAction SilentlyContinue) {
    node "$scriptDir\install-skills.js" @args
} else {
    Write-Warning "[Auto-Skills] Node.js not found in PATH, verifying basic skills folder..."
    $skillsPath = Join-Path $rootDir "skills"
    if (Test-Path $skillsPath) {
        $count = (Get-ChildItem $skillsPath -Directory).Count
        Write-Host "[Auto-Skills] Detected $count skills in $skillsPath" -ForegroundColor Green
    }
}

