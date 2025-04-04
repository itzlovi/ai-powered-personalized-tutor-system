# AI-Powered Personalized Tutor System 🚀

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/ML-ScikitLearn-orange?logo=scikit-learn" alt="ML">
  <img src="https://img.shields.io/badge/NLP-NLTK%20%7C%20SpaCy-yellowgreen" alt="NLP">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</div>

## 📌 Overview
An intelligent tutoring system developed for **Intel® Unnati Industrial Training 2025** that personalizes K-12 education using AI/ML. The system adapts to each student's learning level and creates customized study materials.

## ✨ Features
- **Smart Predictions**: Forecasts student performance (85% accuracy target)
- **Adaptive Learning**: Adjusts content difficulty in real-time
- **Personalized Paths**: Recommends ideal study materials
- **Promotion Advisor**: Suggests class promotion with 50% confidence
- **NLP Magic**: Simplifies/complexifies text automatically

## 🛠️ Installation
```bash
# 1. Clone the repo
git clone https://github.com/yourusername/ai-tutor.git
cd ai-tutor

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt
🚀 How to Use
Command Line:

bash
Copy
python src/main.py --student ST001 --subject Math
Web Interface:

bash
Copy
streamlit run src/streamlit_app.py
📂 Project Structure
Copy
ai-tutor/
├── data/               # All datasets
├── docs/               # Documentation
├── models/             # Trained ML models
├── src/
│   ├── core/           # Main logic
│   ├── utils/          # Helpers
│   ├── main.py         # CLI app
│   └── app.py         # Web interface
├── tests/              # Test cases
├── README.md           # This file
└── requirements.txt    # Dependencies
🤖 Technologies Used
Machine Learning: Scikit-learn, TensorFlow

Natural Language Processing: NLTK, SpaCy

Data Handling: Pandas, NumPy

Visualization: Matplotlib, Plotly

Web Framework: Streamlit

🤝 Contribute
Fork the project

Create your branch (git checkout -b cool-feature)

Commit changes (git commit -m 'Added cool feature')

Push (git push origin cool-feature)

Open a Pull Request

📜 License
MIT License - See LICENSE file
