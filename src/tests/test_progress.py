import joblib

# Define the missing class
class EqualFeatureImportanceClassifier:
    def __init__(self):
        pass  # Add any required initialization here

    def predict(self, X):
        pass  # Implement prediction logic here

# Now load the model
model_path = r"C:\Users\Lovepreet\OneDrive\Documents\Intel Project - Copy\student_performance_model.pkl"

try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
