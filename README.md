# ai-powered-personalized-tutor-system

An intelligent adaptive learning platform that:  📊 Predicts student performance using ML models (85% accuracy target)  🎯 Recommends personalized learning paths based on cognitive levels 👍 Dynamically adapts study materials using NLP (text simplification/enhancement) 📝 Makes promotion decisions with 50% confidence threshold

## Overview

This project is an AI-powered adaptive learning system that personalizes educational content for students based on their individual learning patterns, performance, and cognitive levels. By leveraging machine learning and natural language processing techniques, the system creates a tailored learning experience for each user.

## Features

- **Personalized Content Generation**: Automatically creates customized learning materials based on student's learning style and progress
- **ML-Based Performance Prediction**: Utilizes machine learning models to predict student outcomes with high accuracy
- **Cognitive Level Assessment**: Evaluates and adapts to students' cognitive capabilities
- **NLP-Enhanced Study Materials**: Simplifies or enhances text content according to student needs
- **Progress Visualization**: Interactive dashboards for monitoring student development
- **Smart Recommendation Engine**: Suggests appropriate learning resources and next steps
- **Streamlit Web Interface**: User-friendly application for students and educators

## Installation

1. Clone the repository
```bash
git clone https://github.com/itzlovi/ai-powered-personalized-tutor-system.git
cd ai-powered-personalized-tutor-system

Set up a virtual environment (recommended)

bashCopypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashCopypip install -r requirements.txt
Usage
Run the main application:
bashCopypython src/main.py
For the Streamlit interface:
bashCopystreamlit run src/streamlit_app.py
Project Structure

assets/: Contains images, datasets, and other static resources
docs/: Documentation files
src/: Source code

data/: Data processing modules and datasets
models/: Machine learning model definitions and training scripts
modules/: Core system modules
utils/: Utility functions and helpers
tests/: Test suites and validation scripts
adaptive_content_generator.py: Main module for content adaptation
model_training.py: Scripts for training ML models
recommendation_engine.py: Course and content recommendation system
streamlit_app.py: Web-based user interface
main.py: Entry point for the application



Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Copy
After entering this content, click the "Commit changes..." button in the top right to save your README file to the repository.
