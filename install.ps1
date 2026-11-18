# Global installer for Windows (Claude Code + Google Antigravity)
$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

$ClaudeSkillDir = Join-Path $HOME ".claude\skills\linkedin-profile-optimizer"
$AgySkillDir    = Join-Path $HOME ".gemini\config\skills\linkedin-profile-optimizer"

foreach ($Target in @($ClaudeSkillDir, $AgySkillDir)) {
    New-Item -ItemType Directory -Force -Path $Target | Out-Null
    Copy-Item -Path (Join-Path $RepoRoot "SKILL.md") -Destination $Target -Force
    Copy-Item -Path (Join-Path $RepoRoot "references") -Destination $Target -Recurse -Force
    Copy-Item -Path (Join-Path $RepoRoot "scripts") -Destination $Target -Recurse -Force
    Write-Host "Installed linkedin-profile-optimizer to: $Target"
}
