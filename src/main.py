from Adaptive_Learning_Content_Generator import AdaptiveLearningContentGenerator
from recommendation_engine import StudyMaterialRecommender

def get_user_input():
    """Gets subject and learning speed from user."""
    print("Available Subjects: Mathematics, Science, English")
    subject = input("Enter subject: ").strip().capitalize()
    
    print("Learning Speed Options: slow, medium, fast")
    learning_speed = input("Enter learning speed: ").strip().lower()
    
    return subject, learning_speed

def main():
    print("===== Adaptive Learning System =====")
    print("This system provides personalized study materials and adaptive content.")
    
    # Get user input
    subject, learning_speed = get_user_input()
    
    # Initialize the recommender
    recommender = StudyMaterialRecommender()
    
    # Get recommendations
    recommendation = recommender.recommend_materials(subject, learning_speed)
    
    if recommendation:
        # Display recommendations
        print("\n===== YOUR PERSONALIZED LEARNING PLAN =====")
        print(f"Subject: {recommendation['subject']}")
        print(f"Learning Level: {recommendation['student_level']}")
        
        print("\n----- RECOMMENDED STUDY MATERIALS -----")
        for i, material in enumerate(recommendation['recommended_materials'], 1):
            print(f"{i}. {material['title']}")
            print(f"   Description: {material['description']}")
            print(f"   URL: {material['url']}")
        
        print("\n----- ADAPTIVE LEARNING CONTENT -----")
        print(f"Topic: {recommendation['adaptive_content']['topic']}")
        print(f"Content tailored for {learning_speed} learners:")
        print(recommendation['adaptive_content']['content'])
        
        print("\n===== HAPPY LEARNING! =====")

if __name__ == "__main__":
    main()