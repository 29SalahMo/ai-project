# Git Setup Script for AI Project
# Run this script to configure git and prepare for GitHub push

Write-Host "=== Git Setup for AI Project ===" -ForegroundColor Cyan
Write-Host ""

# Get user information
$userName = Read-Host "Enter your name (for git commits)"
$userEmail = Read-Host "Enter your email (for git commits)"

# Configure git
Write-Host "`nConfiguring git..." -ForegroundColor Yellow
git config user.name "$userName"
git config user.email "$userEmail"

Write-Host "Git configured successfully!" -ForegroundColor Green
Write-Host ""

# Create initial commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
git add .
git commit -m "Initial commit: AI Project with interactive web interface - Search algorithms and ML classifier"

Write-Host "`n✅ Initial commit created!" -ForegroundColor Green
Write-Host ""

# Instructions
Write-Host "=== Next Steps ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Create a repository on GitHub:"
Write-Host "   Go to: https://github.com/new" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. After creating the repository, run these commands:"
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/ai-project.git" -ForegroundColor Yellow
Write-Host "   git branch -M main" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "3. Deploy to Streamlit Cloud:"
Write-Host "   Go to: https://share.streamlit.io" -ForegroundColor Yellow
Write-Host ""
Write-Host "See QUICK_START.md for detailed instructions!" -ForegroundColor Cyan
Write-Host ""
