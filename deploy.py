#!/usr/bin/env python3
"""
Quick deployment script for Image Captioning App
Helps you deploy to various platforms with guided setup
"""

import subprocess
import sys
import os

def run_command(cmd, description=""):
    """Run a command and handle errors"""
    print(f"🔄 {description}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description}")
        print(f"Error: {e.stderr}")
        return None

def check_git():
    """Check if git is initialized and has commits"""
    if not os.path.exists('.git'):
        print("📝 Initializing git repository...")
        run_command("git init", "Initialize git")
        run_command("git add .", "Add files to git")
        run_command('git commit -m "Initial commit"', "Create initial commit")
    else:
        print("✅ Git repository found")

def deploy_railway():
    """Deploy to Railway"""
    print("\n🚂 Deploying to Railway...")
    print("1. Make sure you have a Railway account")
    print("2. Install Railway CLI: npm install -g @railway/cli")
    print("3. Run: railway login")
    print("4. Run: railway init")
    print("5. Run: railway up")
    
    choice = input("\nDo you want to try automatic Railway deployment? (y/n): ")
    if choice.lower() == 'y':
        if run_command("railway --version", "Check Railway CLI"):
            run_command("railway up", "Deploy to Railway")
        else:
            print("❌ Railway CLI not found. Please install it first.")

def deploy_heroku():
    """Deploy to Heroku"""
    print("\n🟣 Deploying to Heroku...")
    
    app_name = input("Enter your Heroku app name (or press Enter to generate): ").strip()
    
    commands = [
        ("heroku --version", "Check Heroku CLI"),
        ("heroku login", "Login to Heroku"),
    ]
    
    if app_name:
        commands.append((f"heroku create {app_name}", f"Create Heroku app: {app_name}"))
    else:
        commands.append(("heroku create", "Create Heroku app"))
    
    commands.extend([
        ("git push heroku main", "Deploy to Heroku"),
        ("heroku open", "Open deployed app")
    ])
    
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            print(f"❌ Failed at: {desc}")
            return

def deploy_docker():
    """Build and run Docker container"""
    print("\n🐳 Building Docker container...")
    
    commands = [
        ("docker --version", "Check Docker"),
        ("docker build -t imgcap-app .", "Build Docker image"),
        ("docker run -d -p 5000:5000 --name imgcap-container imgcap-app", "Run container")
    ]
    
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            print(f"❌ Failed at: {desc}")
            return
    
    print("✅ Docker container running at http://localhost:5000")

def main():
    print("🚀 Image Captioning App Deployment Helper")
    print("=" * 50)
    
    # Check git
    check_git()
    
    print("\nChoose deployment option:")
    print("1. Railway (Recommended - Easy)")
    print("2. Heroku (Popular)")
    print("3. Docker (Local)")
    print("4. Show manual instructions")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        deploy_railway()
    elif choice == "2":
        deploy_heroku()
    elif choice == "3":
        deploy_docker()
    elif choice == "4":
        print("\n📖 Manual deployment instructions:")
        print("See DEPLOYMENT.md for detailed instructions")
        print("Quick links:")
        print("- Railway: https://railway.app")
        print("- Heroku: https://heroku.com")
        print("- Google Cloud Run: https://cloud.google.com/run")
        print("- Render: https://render.com")
    elif choice == "5":
        print("👋 Goodbye!")
        sys.exit(0)
    else:
        print("❌ Invalid choice")
        main()

if __name__ == "__main__":
    main()