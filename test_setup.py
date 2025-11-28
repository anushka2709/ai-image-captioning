#!/usr/bin/env python3
"""Test script to verify the ML model setup"""

print("🧪 Testing Image Captioning Setup...")

try:
    print("📦 Testing imports...")
    import torch
    print(f"✅ PyTorch {torch.__version__}")
    
    import transformers
    print(f"✅ Transformers {transformers.__version__}")
    
    from transformers import BlipProcessor, BlipForConditionalGeneration
    print("✅ BLIP imports successful")
    
    print("\n🤖 Testing model loading...")
    from infer import ImageCaptioner
    captioner = ImageCaptioner()
    
    if captioner.model_loaded:
        print("🎉 ML model loaded successfully!")
        print("🚀 Ready for AI-powered image captioning!")
    else:
        print("⚠️  Running in fallback mode")
        print("📝 Will use rule-based captions")
    
    print("\n✅ Setup test complete!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 Try running: pip install -r requirements.txt")
except Exception as e:
    print(f"❌ Setup error: {e}")
    print("💡 Check the error message above for details")