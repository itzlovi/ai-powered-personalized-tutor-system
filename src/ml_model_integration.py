import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from study_material_recommender import print_recommendations

def create_sample_dataset():
    """Generate synthetic student data with improved features"""
    np.random.seed(42)
    n_samples = 1000
    
    # New features - no duplicates
    current_test = np.random.uniform(0, 100, n_samples)  # Latest exam score
    study_hours = np.random.uniform(0, 20, n_samples)    # Weekly study hours
    attendance = np.random.uniform(60, 100, n_samples)    # Attendance percentage
    assignments = np.random.uniform(0, 100, n_samples)    # Assignment scores
    
    # Create labels
    y = []
    for score in current_test:
        if score < 40:
            y.append('Beginner')
        elif 40 <= score < 70:
            y.append('Intermediate')
        else:
            y.append('Advanced')
    
    # Feature matrix with 4 distinct features
    X = np.column_stack([current_test, study_hours, attendance, assignments])
    return X, np.array(y)

def train_student_level_model():
    """Train the classification model"""
    X, y = create_sample_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = LogisticRegression(multi_class='multinomial', max_iter=1000)
    model.fit(X_train_scaled, y_train)
    
    return model, scaler

class StudentLevelPredictor:
    def __init__(self):
        self.model, self.scaler = train_student_level_model()
    
    def predict_student_level(self, current_score, study_hours, attendance, assignments):
        """Predict level using all 4 features"""
        features = np.array([[current_score, study_hours, attendance, assignments]])
        features_scaled = self.scaler.transform(features)
        probabilities = self.model.predict_proba(features_scaled)[0]
        return self.model.classes_[np.argmax(probabilities)]

def get_student_input():
    """Interactive input for student data"""
    print("\n📝 Apna Student Profile Banaaye:")
    
    while True:
        try:
            current_score = float(input("Latest exam score (0-100): "))
            if not 0 <= current_score <= 100:
                print("Please enter between 0-100")
                continue
                
            study_hours = float(input("Weekly padhai ke hours (0-20): "))
            if not 0 <= study_hours <= 20:
                print("Please enter between 0-20")
                continue
                
            attendance = float(input("Class attendance percentage (60-100): "))
            if not 60 <= attendance <= 100:
                print("Please enter between 60-100")
                continue
                
            assignments = float(input("Average assignment marks (0-100): "))
            if not 0 <= assignments <= 100:
                print("Please enter between 0-100")
                continue
                
            return current_score, study_hours, attendance, assignments
            
        except ValueError:
            print("Please enter valid numbers only")

def recommend_materials_for_student():
    """Complete prediction pipeline"""
    # Get student input
    current_score, study_hours, attendance, assignments = get_student_input()
    
    # Make prediction
    predictor = StudentLevelPredictor()
    level = predictor.predict_student_level(current_score, study_hours, attendance, assignments)
    
    # Show results
    print(f"\n🎯 Aapka Result:")
    print(f"Latest Exam: {current_score}")
    print(f"Study Hours/Week: {study_hours}")
    print(f"Attendance: {attendance}%")
    print(f"Assignments: {assignments}")
    print(f"Predicted Level: {level}")
    
    # Get recommendations
    print("\n📚 Aapke Liye Recommendation:")
    print_recommendations(level)

def main():
    print("🌟 Student Level Predictor 🌟")
    print("Yeh program aapke learning level ka pata lagata hai\n")
    
    while True:
        recommend_materials_for_student()
        
        repeat = input("\nKya aap dubara check karna chahenge? (haan/na): ").lower()
        if repeat not in ('haan', 'h', 'yes', 'y'):
            print("\nDhanyavaad, program ko istemal karne ke liye!")
            break

if __name__ == "__main__":
    main()