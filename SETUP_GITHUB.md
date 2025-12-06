# GitHub Repository Setup Instructions

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `Gform_COD_Status`
3. Description: `G-Form COD Status Email Automation - Automated email reporting system`
4. Choose visibility (Public or Private)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 2: Push to GitHub

After creating the repository on GitHub, run these commands:

```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Gform_COD_Status.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Alternative: Using SSH

If you prefer SSH:

```bash
git remote add origin git@github.com:YOUR_USERNAME/Gform_COD_Status.git
git branch -M main
git push -u origin main
```

## Quick Setup Script

You can also run the provided script:

```bash
python setup_github.py
```

(Enter your GitHub username when prompted)

