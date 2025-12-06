"""
Helper script to set up GitHub remote and push the repository
"""

import subprocess
import sys
import os

def run_command(cmd, check=True):
    """Run a git command"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def main():
    print("="*60)
    print("GitHub Repository Setup")
    print("="*60)
    
    # Get GitHub username
    username = input("Enter your GitHub username: ").strip()
    if not username:
        print("❌ Username cannot be empty")
        return
    
    # Check if remote already exists
    result = run_command("git remote -v", check=False)
    if "origin" in result:
        print("⚠️  Remote 'origin' already exists")
        overwrite = input("Do you want to update it? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Cancelled.")
            return
        run_command("git remote remove origin", check=False)
    
    # Add remote
    repo_url = f"https://github.com/{username}/Gform_COD_Status.git"
    print(f"\n📦 Adding remote: {repo_url}")
    result = run_command(f'git remote add origin {repo_url}')
    if result is None:
        print("❌ Failed to add remote")
        return
    
    # Check current branch
    current_branch = run_command("git branch --show-current")
    if current_branch != "main":
        print(f"\n🔄 Renaming branch from '{current_branch}' to 'main'")
        run_command("git branch -M main")
    
    print("\n✅ Remote configured successfully!")
    print("\n" + "="*60)
    print("Next Steps:")
    print("="*60)
    print("1. Create the repository on GitHub:")
    print(f"   Go to: https://github.com/new")
    print(f"   Repository name: Gform_COD_Status")
    print(f"   DO NOT initialize with README, .gitignore, or license")
    print("\n2. After creating the repository, run:")
    print("   git push -u origin main")
    print("="*60)

if __name__ == "__main__":
    main()

