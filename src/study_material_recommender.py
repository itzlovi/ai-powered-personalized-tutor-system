import pandas as pd
from pathlib import Path
import random

class StudyMaterialRecommender:
    def __init__(self):
        self.df = self.load_study_materials()
        self.valid_levels = ['Beginner', 'Intermediate', 'Advanced']
        self.valid_subjects = ['Math', 'Science', 'English']

    def load_study_materials(self):
        """Load and validate study materials database"""
        try:
            if not Path('study_materials_database.csv').exists():
                self.create_sample_csv()
            
            df = pd.read_csv('study_materials_database.csv')
            
            # Validate required columns
            required_columns = ['level', 'subject', 'material_type', 'resource_name']
            missing_cols = [col for col in required_columns if col not in df.columns]
            
            if missing_cols:
                raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")
                
            return df
            
        except Exception as e:
            print(f"Error loading study materials: {str(e)}")
            return None

    def create_sample_csv(self):
        """Create sample CSV if not exists"""
        sample_data = {
            'level': ['Beginner']*4 + ['Intermediate']*4 + ['Advanced']*4,
            'subject': ['Math', 'Math', 'Science', 'English']*3,
            'material_type': ['Video', 'Book', 'Video', 'Book']*3,
            'resource_name': [
                'Basic Arithmetic Concepts', 'Mathematics for Beginners', 
                'Introduction to Science', 'Simple English Stories',
                'Algebra Fundamentals', 'Geometry Problems',
                'Chemistry Basics', 'Grammar Rules',
                'Trigonometry Masterclass', 'Calculus Concepts',
                'Quantum Physics', 'Essay Writing Techniques'
            ],
            'difficulty': ['Easy']*4 + ['Medium']*4 + ['Hard']*4,
            'link': [
                'https://example.com/math-basic', 'https://example.com/math-book',
                'https://example.com/science-intro', 'https://example.com/english-stories',
                'https://example.com/algebra', 'https://example.com/geometry-problems',
                'https://example.com/chemistry-basics', 'https://example.com/grammar-rules',
                'https://example.com/trigonometry', 'https://example.com/calculus',
                'https://example.com/quantum-physics', 'https://example.com/essay-writing'
            ],
            'tags': [
                'foundation basics', 'starter fundamentals', 'basic concepts', 'reading beginner',
                'equations algebra', 'shapes practice', 'elements reactions', 'rules writing',
                'angles advanced', 'derivatives integrals', 'particles theory', 'composition advanced'
            ]
        }
        pd.DataFrame(sample_data).to_csv('study_materials_database.csv', index=False)
        print("Created sample study materials database")

    def get_recommendations(self, predicted_level, subject=None, num_recommendations=3):
        """Get personalized recommendations"""
        if self.df is None:
            return None
            
        if predicted_level not in self.valid_levels:
            raise ValueError(f"Invalid level. Must be one of: {', '.join(self.valid_levels)}")
            
        if subject and subject not in self.valid_subjects:
            raise ValueError(f"Invalid subject. Must be one of: {', '.join(self.valid_subjects)}")
            
        # Filter materials
        filtered = self.df[self.df['level'] == predicted_level]
        if subject:
            filtered = filtered[filtered['subject'] == subject]
        
        # Select random recommendations if available
        if not filtered.empty:
            if len(filtered) > num_recommendations:
                filtered = filtered.sample(n=num_recommendations)
            return filtered.to_dict('records')
        return None

    def print_recommendations(self, predicted_level, subject=None):
        """Display recommendations in user-friendly format"""
        try:
            recommendations = self.get_recommendations(predicted_level, subject)
            
            if not recommendations:
                print(f"\nNo recommendations found for {predicted_level} level")
                if subject:
                    print(f"in {subject} subject")
                return
                
            print(f"\n🎯 Recommended Study Materials ({predicted_level} Level):")
            print("="*60)
            for material in recommendations:
                print(f"\nSubject: {material['subject']}")
                print(f"Type: {material['material_type']}")
                print(f"Resource: {material['resource_name']}")
                print(f"Difficulty: {material['difficulty']}")
                if pd.notna(material.get('link')):
                    print(f"Link: {material['link']}")
                if pd.notna(material.get('tags')):
                    print(f"Tags: {material['tags']}")
            print("="*60)
            
        except Exception as e:
            print(f"\nError generating recommendations: {str(e)}")

# Standalone functions for easy integration
def get_recommendations(level, subject=None):
    """Standalone function to get recommendations"""
    recommender = StudyMaterialRecommender()
    return recommender.get_recommendations(level, subject)

def print_recommendations(level, subject=None):
    """Standalone function to print recommendations"""
    recommender = StudyMaterialRecommender()
    return recommender.print_recommendations(level, subject)

if __name__ == "__main__":
    # Test the recommender
    recommender = StudyMaterialRecommender()
    print("\nTesting Recommendation System:")
    test_cases = [
        ("Beginner", None),
        ("Intermediate", "Math"),
        ("Advanced", "Science"),
        ("Invalid", "English")
    ]
    for level, subject in test_cases:
        print(f"\nCase: Level={level}, Subject={subject}")
        recommender.print_recommendations(level, subject)