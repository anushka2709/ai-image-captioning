🤖📷 AI-Powered Image Caption Generator

Upload an image and let AI describe what it sees ⚡
A deep learning–based Image Captioning App deployed on Render.

🔴 Live Demo:
👉 https://ai-image-captioning-daoi.onrender.com

📌 Features

-Upload any image and get captions
-AI-powered inference
-Fast and lightweight Flask backend
-Clean UI & mobile responsive
-Fully deployed on Render

🧠 Why It Works?

-CNN extracts visual features from image
-LSTM Decoder generates meaningful sentences
-Pretrained vocabulary and rule-based fallback

📂 Project Structure
ai-image-captioning/
│── app.py
│── encoder.py
│── decoder.py
│── infer.py
│── requirements.txt
│── Procfile
│── railway.toml
│── Dockerfile
│── templates/
│── data/
└── README.md

🔧 Run Locally
git clone https://github.com/anushka2709/ai-image-captioning.git
cd ai-image-captioning
pip install -r requirements.txt
python app.py

🚀 Deploy on Render
Build Command:
pip install -r requirements.txt
Start Command:
python app.py
Render automatically sets PORT 👌

🔮 Future Scope

-Transformer-based model for better captions
-Dark theme UI
-Multi-language captioning
-Store caption results

👩‍💻 Author

Anushka Bohra 💜
⭐ Star the repo if you like it!
