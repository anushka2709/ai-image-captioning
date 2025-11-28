@echo off
echo 🚀 Quick Deploy Script
echo.

echo Step 1: Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
echo git remote add origin https://github.com/YOUR_USERNAME/ai-image-captioning.git
echo.

echo Step 2: Push to GitHub
echo git push -u origin master
echo.

echo Step 3: Deploy to Railway
echo 1. Go to https://railway.app
echo 2. Click "Deploy from GitHub repo"
echo 3. Select "ai-image-captioning"
echo 4. Click Deploy!
echo.

echo Your app will be live in 2 minutes! 🎉
pause