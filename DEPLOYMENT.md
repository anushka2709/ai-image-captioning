# 🚀 Deployment Guide

This guide covers multiple deployment options for your AI Image Captioning app.

## 📋 Prerequisites

- Git repository with your code
- Account on your chosen platform
- Basic command line knowledge

## 🌐 Deployment Options

### 1. Railway (Recommended - Easiest)

Railway offers the simplest deployment with automatic builds.

**Steps:**
1. Push your code to GitHub
2. Go to [Railway.app](https://railway.app)
3. Click "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect and deploy!

**Configuration:**
- Uses `railway.toml` for settings
- Automatic HTTPS
- Custom domains available
- Built-in monitoring

### 2. Heroku (Popular Choice)

**Steps:**
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

**Configuration:**
```bash
# Set environment variables
heroku config:set FLASK_ENV=production
heroku config:set WEB_CONCURRENCY=1

# Scale dynos
heroku ps:scale web=1
```

### 3. Google Cloud Run (Serverless)

**Steps:**
1. Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
2. Authenticate: `gcloud auth login`
3. Set project: `gcloud config set project YOUR_PROJECT_ID`
4. Deploy: `gcloud run deploy --source .`

**Benefits:**
- Pay per request
- Auto-scaling
- HTTPS included
- Global CDN

### 4. AWS App Runner

**Steps:**
1. Push code to GitHub
2. Go to AWS App Runner console
3. Create service from source code
4. Connect GitHub repository
5. Configure build settings

**Configuration:**
```yaml
# apprunner.yaml
version: 1.0
runtime: python3
build:
  commands:
    build:
      - pip install -r requirements.txt
run:
  runtime-version: 3.10
  command: gunicorn app:app --bind 0.0.0.0:8000
  network:
    port: 8000
    env: PORT
```

### 5. DigitalOcean App Platform

**Steps:**
1. Go to DigitalOcean Apps
2. Create new app from GitHub
3. Select repository and branch
4. Configure build settings
5. Deploy

### 6. Render (Free Tier Available)

**Steps:**
1. Connect GitHub to [Render](https://render.com)
2. Create new Web Service
3. Select repository
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`

## 🐳 Docker Deployment

### Local Docker
```bash
# Build image
docker build -t imgcap-app .

# Run container
docker run -p 5000:5000 imgcap-app
```

### Docker Compose
```bash
# Start services
docker-compose up --build

# Run in background
docker-compose up -d
```

### Docker Hub
```bash
# Tag and push
docker tag imgcap-app yourusername/imgcap-app
docker push yourusername/imgcap-app
```

## ⚙️ Environment Variables

Set these for production:

```bash
FLASK_ENV=production
WEB_CONCURRENCY=1
MAX_WORKERS=1
TIMEOUT=120
```

## 🔧 Performance Optimization

### Memory Management
- Use `--max-requests 100` to restart workers periodically
- Set `WEB_CONCURRENCY=1` for memory-constrained environments
- Consider using CPU-only PyTorch for smaller memory footprint

### Caching
- Model files are cached after first load
- Consider using Redis for session caching in high-traffic scenarios

### Monitoring
- Enable health checks: `/health` endpoint
- Monitor memory usage
- Set up alerts for response times

## 🚨 Troubleshooting

### Common Issues

**Memory Errors:**
- Reduce image size before processing
- Use CPU-only PyTorch
- Increase server memory

**Timeout Errors:**
- Increase timeout settings
- Optimize model loading
- Use async processing for large images

**Build Failures:**
- Check Python version compatibility
- Verify all dependencies in requirements.txt
- Check for system dependencies

### Debug Commands
```bash
# Check logs
heroku logs --tail  # Heroku
railway logs        # Railway
docker logs <container_id>  # Docker

# Test locally
python app.py
curl -X POST -F "image=@test.jpg" http://localhost:5000/caption
```

## 📊 Cost Estimates

| Platform | Free Tier | Paid Plans |
|----------|-----------|------------|
| Railway | 500 hours/month | $5+/month |
| Heroku | 550 hours/month | $7+/month |
| Google Cloud Run | 2M requests/month | Pay per use |
| Render | 750 hours/month | $7+/month |
| AWS App Runner | None | $0.064/vCPU hour |

## 🎯 Recommended Setup

For **development**: Railway or Render (free tier)
For **production**: Google Cloud Run or AWS App Runner
For **enterprise**: Kubernetes with custom scaling

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review platform-specific documentation
3. Check GitHub issues
4. Contact platform support

Happy deploying! 🚀