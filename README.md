# AI-Powered Personalized Tutor System 🚀

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/ML-ScikitLearn-orange?logo=scikit-learn" alt="ML">
  <img src="https://img.shields.io/badge/NLP-NLTK%20%7C%20SpaCy-yellowgreen" alt="NLP">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</div>

## 📌 Overview
AI-Powered Personalized Tutor System is a fully automated AI-driven educational tool developed for **Intel® Unnati Industrial Training 2025**. It personalizes K-12 education using AI/ML, adapting to each student's learning level and creating customized study materials.

## Demo Video
(https://youtu.be/0HUHqJv4xww)

## Output Images
Here are some sample outputs generated by the AI-powered tutoring system.

## Project Overview
AI-Powered Personalized Tutor System follows the following pipeline:

1. **Smart Predictions**: Forecasts student performance with an 85% accuracy target.
2. **Adaptive Learning**: Adjusts content difficulty in real-time.
3. **Personalized Paths**: Recommends ideal study materials.
4. **Promotion Advisor**: Suggests class promotion with 50% confidence.
5. **NLP Magic**: Simplifies/complexifies text automatically.

## Features
- **AI-Powered Learning**: Generates customized study materials and adaptive content.
- **Performance Prediction**: Uses machine learning to predict student progress.
- **Personalized Recommendations**: Suggests study paths based on student performance.
- **NLP-Based Assistance**: Enhances text comprehension and simplification.
- **Web Interface**: Built with Streamlit for seamless interaction.

## Tech Stack
- **Programming Language**: Python
- **Framework**: Streamlit
- **Machine Learning**: Scikit-learn, TensorFlow
- **Natural Language Processing**: NLTK, SpaCy
- **Data Handling**: Pandas, NumPy
- **Visualization**: Matplotlib, Plotly

## Project Structure
```
ai-tutor/
├── data/               # All datasets
├── docs/               # Documentation
├── models/             # Trained ML models
├── src/
│   ├── core/           # Main logic
│   ├── utils/          # Helpers
│   ├── main.py         # CLI app
│   ├── app.py          # Web interface
│   ├── process_data.py # Data processing module
├── tests/              # Test cases
├── output/             # Generated reports
├── .env                # API keys and environment variables
├── requirements.txt    # Dependencies
└── README.md           # This file
```

## Installation and Setup
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-tutor.git  
cd ai-tutor
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Add API Keys
Create a `.env` file in the root directory and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key  
NLP_API_KEY=your_nlp_api_key
```
### 4. Run the Application
```bash
streamlit run src/streamlit_app.py
```

## Contributing
Contributions are welcome!

If you have improvements, bug fixes, or new feature ideas:
1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Commit and push your changes.
4. Submit a pull request.

Feel free to experiment and enhance the AI-powered tutoring system!

## 📜 License
MIT License - See LICENSE file

