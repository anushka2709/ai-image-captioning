# 🤖 AI Image Captioning App

A beautiful, modern web application that generates intelligent captions for uploaded images using state-of-the-art BLIP AI model from Hugging Face.

![App Preview](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3+-red)
![AI](https://img.shields.io/badge/AI-BLIP%20Model-purple)

## ✨ Features

- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 🖼️ **Drag & Drop**: Intuitive image upload with visual feedback
- 🤖 **AI-Powered**: Uses BLIP (Bootstrapping Language-Image Pre-training) model
- 📱 **Responsive**: Works perfectly on desktop and mobile
- ⚡ **Fast**: Optimized for quick caption generation
- 🔄 **Fallback**: Graceful degradation with rule-based captions
- 🌐 **Production Ready**: Multiple deployment options included

## 🚀 Quick Start

### Option 1: One-Click Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

### Option 2: Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd imgcap_app

# Run setup script
python setup.py

# Start the application
python app.py
```

Visit `http://localhost:5000` to see your app in action!

## 🛠️ Manual Setup

### Prerequisites
- Python 3.10+
- 4GB+ RAM (for AI model)
- Modern web browser

### Installation

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

## 🌐 Deployment

We support multiple deployment platforms. Choose what works best for you:

### 🚂 Railway (Recommended)
- **Pros**: Easiest setup, automatic HTTPS, great free tier
- **Steps**: Connect GitHub → Deploy → Done!
- [Detailed Guide](DEPLOYMENT.md#railway)

### 🟣 Heroku
- **Pros**: Popular, lots of documentation
- **Steps**: `heroku create` → `git push heroku main`
- [Detailed Guide](DEPLOYMENT.md#heroku)

### ☁️ Google Cloud Run
- **Pros**: Serverless, pay-per-request, auto-scaling
- **Steps**: `gcloud run deploy --source .`
- [Detailed Guide](DEPLOYMENT.md#google-cloud-run)

### 🐳 Docker
```bash
# Build and run
docker build -t imgcap-app .
docker run -p 5000:5000 imgcap-app

# Or use docker-compose
docker-compose up --build
```

### 📋 Quick Deploy Script
```bash
python deploy.py
```

## 🎯 API Usage

### Caption Generation Endpoint

**POST** `/caption`

```javascript
const formData = new FormData();
formData.append('image', imageFile);

fetch('/caption', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => {
    console.log('Caption:', data.caption);
});
```

### Health Check Endpoint

**GET** `/health`

```json
{
    "status": "healthy",
    "model_loaded": true,
    "fallback_mode": false
}
```

## 🧠 How It Works

1. **Image Upload**: User uploads image via drag & drop or file picker
2. **Preprocessing**: Image is resized and normalized for optimal processing
3. **AI Analysis**: BLIP model analyzes the image and generates descriptive text
4. **Caption Display**: Generated caption is displayed with smooth animations
5. **Fallback**: If AI fails, rule-based system provides basic descriptions

## 🔧 Configuration

### Environment Variables

```bash
FLASK_ENV=production          # Set to production for deployment
WEB_CONCURRENCY=1            # Number of worker processes
MAX_WORKERS=1                # Max workers (memory optimization)
TIMEOUT=120                  # Request timeout in seconds
```

### Model Configuration

The app automatically:
- Downloads BLIP model on first run (~1GB)
- Caches model files for faster subsequent loads
- Falls back to rule-based captions if model fails

## 📊 Performance

- **First Load**: ~10-15 seconds (model download)
- **Subsequent Loads**: ~2-3 seconds
- **Memory Usage**: ~2-3GB with AI model
- **Supported Formats**: PNG, JPG, JPEG, GIF, BMP
- **Max Image Size**: 16MB

## 🐛 Troubleshooting

### Common Issues

**Memory Errors:**
```bash
# Use CPU-only version
pip install torch==2.0.1+cpu torchvision==0.15.2+cpu
```

**Model Loading Fails:**
- Check internet connection (model downloads from Hugging Face)
- Ensure sufficient disk space (~2GB)
- Try restarting the application

**Slow Performance:**
- Use smaller images (<2MB)
- Consider GPU deployment for faster processing
- Enable caching for repeated requests

### Debug Mode
```bash
FLASK_ENV=development python app.py
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Salesforce BLIP](https://github.com/salesforce/BLIP) for the amazing AI model
- [Hugging Face](https://huggingface.co/) for model hosting and transformers library
- [Flask](https://flask.palletsprojects.com/) for the web framework

## 📞 Support

- 📖 [Deployment Guide](DEPLOYMENT.md)
- 🐛 [Report Issues](https://github.com/your-repo/issues)
- 💬 [Discussions](https://github.com/your-repo/discussions)

---

Made with ❤️ and 🤖 AI