from PIL import Image
import io
import os

class ImageCaptioner:
    def __init__(self):
        self.model_loaded = False
        self.fallback_mode = True
        
        try:
            # Try to import ML libraries
            import torch
            from transformers import BlipProcessor, BlipForConditionalGeneration
            
            print("Loading BLIP model...")
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            print(f"Using device: {self.device}")
            
            # Load model with error handling
            model_name = "Salesforce/blip-image-captioning-base"
            self.processor = BlipProcessor.from_pretrained(model_name)
            self.model = BlipForConditionalGeneration.from_pretrained(
                model_name,
                torch_dtype=torch.float32,
                low_cpu_mem_usage=True
            )
            self.model.to(self.device)
            self.model.eval()
            
            self.model_loaded = True
            self.fallback_mode = False
            print("✅ BLIP model loaded successfully!")
            
        except ImportError as e:
            print(f"⚠️  ML libraries not available: {e}")
            print("📝 Running in fallback mode with rule-based captions")
        except Exception as e:
            print(f"⚠️  Error loading BLIP model: {e}")
            print("📝 Running in fallback mode with rule-based captions")
        
    def generate_caption(self, image_bytes):
        """Generate caption for image from bytes"""
        if self.model_loaded and not self.fallback_mode:
            return self._generate_ml_caption(image_bytes)
        else:
            return self._generate_fallback_caption(image_bytes)
    
    def _generate_ml_caption(self, image_bytes):
        """Generate caption using BLIP model"""
        try:
            import torch
            
            # Load and preprocess image
            image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            print(f"🖼️  Processing image: {image.size}")
            
            # Resize if too large
            max_size = 512
            if max(image.size) > max_size:
                image.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                print(f"📏 Resized to: {image.size}")
            
            # Process image
            inputs = self.processor(image, return_tensors="pt")
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # Generate caption
            with torch.no_grad():
                generated_ids = self.model.generate(
                    **inputs,
                    max_length=50,
                    num_beams=5,
                    early_stopping=True,
                    do_sample=False,
                    repetition_penalty=1.1
                )
            
            # Decode caption
            caption = self.processor.decode(generated_ids[0], skip_special_tokens=True)
            print(f"🤖 Generated: {caption}")
            
            return caption
            
        except Exception as e:
            print(f"❌ ML caption failed: {e}")
            print("🔄 Falling back to rule-based caption")
            return self._generate_fallback_caption(image_bytes)
    
    def _generate_fallback_caption(self, image_bytes):
        """Generate caption using rule-based approach"""
        try:
            image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            width, height = image.size
            aspect_ratio = width / height
            
            # Analyze colors
            colors = image.getcolors(maxcolors=256*256*256)
            if colors:
                dominant_color = max(colors, key=lambda x: x[0])[1]
                r, g, b = dominant_color
                
                if r > 200 and g > 200 and b > 200:
                    color_desc = "bright and light"
                elif r < 50 and g < 50 and b < 50:
                    color_desc = "dark and moody"
                elif r > g + 50 and r > b + 50:
                    color_desc = "warm with red tones"
                elif g > r + 50 and g > b + 50:
                    color_desc = "natural with green tones"
                elif b > r + 50 and b > g + 50:
                    color_desc = "cool with blue tones"
                else:
                    color_desc = "colorful and vibrant"
            else:
                color_desc = "visually interesting"
            
            # Determine composition
            if aspect_ratio > 1.8:
                composition = "panoramic landscape"
            elif aspect_ratio > 1.3:
                composition = "wide composition"
            elif aspect_ratio < 0.6:
                composition = "tall portrait"
            elif aspect_ratio < 0.8:
                composition = "vertical composition"
            else:
                composition = "balanced square composition"
            
            # Generate varied captions
            captions = [
                f"An image with {color_desc} colors in a {composition}",
                f"A {color_desc} photograph featuring a {composition}",
                f"A visually appealing image with {color_desc} tones and {composition}",
                f"An artistic image showcasing {color_desc} elements in {composition}"
            ]
            
            # Pick caption based on image properties
            caption_index = (width + height + sum([r, g, b] if colors else [0, 0, 0])) % len(captions)
            caption = captions[caption_index]
            
            print(f"📝 Rule-based caption: {caption}")
            return caption
            
        except Exception as e:
            print(f"❌ Fallback caption failed: {e}")
            return "A beautiful and interesting image worth sharing."