#!/usr/bin/env python3
"""
Setup script for Image Captioning App
This script handles the installation of dependencies with proper version management
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {cmd}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {cmd}")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🚀 Setting up Image Captioning App...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version}")
    
    # Install dependencies in correct order
    dependencies = [
        "pip install --upgrade pip",
        "pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu",
        "pip install transformers==4.30.2",
        "pip install tokenizers==0.13.3",
        "pip install flask==2.3.3",
        "pip install pillow==10.0.0",
        "pip install requests==2.31.0",
        "pip install gunicorn==21.2.0"
    ]
    
    success_count = 0
    for cmd in dependencies:
        if run_command(cmd):
            success_count += 1
        else:
            print(f"⚠️  Failed to install: {cmd}")
    
    print(f"\n📊 Installation Summary: {success_count}/{len(dependencies)} successful")
    
    if success_count == len(dependencies):
        print("🎉 Setup complete! You can now run: python app.py")
    else:
        print("⚠️  Some dependencies failed. The app will run in fallback mode.")
    
    # Test the setup
    print("\n🧪 Testing setup...")
    try:
        from infer import ImageCaptioner
        captioner = ImageCaptioner()
        print("✅ Image captioner initialized successfully")
    except Exception as e:
        print(f"⚠️  Setup test failed: {e}")

if __name__ == "__main__":
    main()