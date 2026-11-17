# ⚡ FULL-STACK PROJECT INITIALIZATION (PowerShell Wrapper)
$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir

Write-Host "[Project-Setup] Executing Full-Stack Setup Engine..." -ForegroundColor Cyan
node "$ProjectRoot\scripts\setup-project.js"

