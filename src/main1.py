import streamlit as st
import joblib
from recommendation_engine import StudyMaterialRecommender

# Define the missing class (Required for loading the model)
class EqualFeatureImportanceClassifier:
    def __init__(self):
        pass

    def predict(self, X):
        return ["Intermediate"]  # Dummy prediction

# Load the trained model
@st.cache_resource
def load_model():
    try:
        model_path = r"C:\Users\Lovepreet\OneDrive\Documents\copy\src\models\student_performance_model.pkl"
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Function to predict the student's next level
def predict_next_level(model, age, test_score, learning_speed, knowledge_level):
    if model:
        input_data = [[age, test_score, learning_speed, knowledge_level]]
        predicted_level = model.predict(input_data)[0]
        return predicted_level
    return "Error: Model could not be loaded."

# Function to provide study material based on subject & level
def get_study_material(subject, level):
    study_materials = {
        "Mathematics": {
            "Beginner": "Math Basics.pdf",
            "Intermediate": "Algebra & Geometry.pdf",
            "Advanced": "Calculus & Trigonometry.pdf",
        },
        "Science": {
            "Beginner": "Science Fundamentals.pdf",
            "Intermediate": "Physics & Chemistry.pdf",
            "Advanced": "Advanced Biology & Physics.pdf",
        },
        "English": {
            "Beginner": "Grammar Basics.pdf",
            "Intermediate": "Essay Writing.pdf",
            "Advanced": "Advanced Literature.pdf",
        },
    }
    return study_materials.get(subject, {}).get(level, "No study material available.")

def main():
    st.set_page_config(page_title="Adaptive Learning System", layout="wide")
    
    # Load model
    model = load_model()
    
    st.title("🎓 Adaptive Learning System")
    st.markdown("This system provides personalized study materials and adaptive content.")
    
    # Create columns for layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Student Information")
        
        # Student inputs
        subject = st.selectbox(
            "Select Subject",
            ["Mathematics", "Science", "English"],
            index=1
        )
        
        learning_speed = st.selectbox(
            "Learning Speed",
            ["slow", "medium", "fast"],
            index=0
        )
        
        age = st.slider("Age", 5, 15, 12)  # Updated age range to 5-15
        test_score = st.slider("Last Test Score (0-100)", 0, 100, 45)
        
        knowledge_level = st.selectbox(
            "Current Knowledge Level",
            ["Beginner", "Intermediate", "Advanced"],
            index=1
        )
        
        if st.button("Get Recommendations"):
            with st.spinner("Generating personalized recommendations..."):
                try:
                    # Predict student's next learning level
                    predicted_level = predict_next_level(model, age, test_score, learning_speed, knowledge_level)
                    
                    # Get study material
                    study_material = get_study_material(subject, predicted_level)
                    
                    # Initialize the recommendation engine
                    recommender = StudyMaterialRecommender()
                    
                    # Get recommendations
                    recommendations = recommender.recommend_materials(
                        subject=subject,
                        learning_speed=learning_speed,
                        student_id="sample_student"
                    )
                    
                    # Display results in col2
                    with col2:
                        st.header("Recommendation Results")
                        
                        # Basic prediction
                        st.subheader("📚 Learning Level Prediction")
                        st.success(f"Your predicted next study level is: **{predicted_level}**")
                        
                        # Basic study material
                        st.subheader("📖 Basic Study Material")
                        st.info(f"Recommended resource: **{study_material}**")
                        
                        # Personalized recommendations
                        st.subheader("🌟 Personalized Recommendations")
                        st.write(f"- **Learning speed:** {recommendations['learning_speed'].capitalize()}")
                        st.write(f"- **Recommended level:** {recommendations['student_level'].capitalize()}")
                        
                        # Recommended materials
                        st.subheader("📚 Recommended Materials")
                        for material in recommendations['recommended_materials']:
                            with st.expander(f"🔗 {material['title']}"):
                                st.write(material['description'])
                                st.markdown(f"[Open Resource]({material['url']})", unsafe_allow_html=True)
                        
                        # Adaptive learning content
                        st.subheader("🧠 Adaptive Learning Content")
                        adaptive_content = recommendations['adaptive_content']
                        with st.expander(f"📖 {adaptive_content['topic']} ({adaptive_content['complexity_level']} level)"):
                            st.write(adaptive_content['content'])
                
                except Exception as e:
                    st.error(f"Error generating recommendations: {e}")
                    st.warning("Showing basic recommendations only...")
                    
                    with col2:
                        st.header("Basic Recommendation")
                        predicted_level = predict_next_level(model, age, test_score, learning_speed, knowledge_level)
                        study_material = get_study_material(subject, predicted_level)
                        st.success(f"Your predicted next study level is: **{predicted_level}**")
                        st.info(f"Recommended resource: **{study_material}**")

if __name__ == "__main__":
    main()