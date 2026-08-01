# GitHub Command Prompt Setup

This workspace includes a PowerShell script to set up Git and the GitHub CLI on Windows.

Files:
- [setup-github-prompt.ps1](setup-github-prompt.ps1)

Run the script from an elevated PowerShell (admin) to install and configure:

```powershell
# Run with prompts
powershell -ExecutionPolicy Bypass -File .\setup-github-prompt.ps1

# Or provide name/email non-interactively
powershell -ExecutionPolicy Bypass -File .\setup-github-prompt.ps1 -Name "Your Name" -Email "you@example.com"
```

Notes:
- `winget` (App Installer) must be available. Install from the Microsoft Store if missing.
- The script runs `gh auth login --web` — follow the browser flow to authenticate.
- Restart your terminal after installation to refresh the PATH.
