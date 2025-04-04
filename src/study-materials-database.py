import pandas as pd

# Create a comprehensive study materials database
study_materials = [
    # Beginner Level Materials
    {"level": "Beginner", "subject": "Math", "material_type": "Basic Arithmetic", "resource_name": "Basic Math Workbook", "difficulty": "Easy"},
    {"level": "Beginner", "subject": "Math", "material_type": "Number Sense", "resource_name": "Counting and Place Value Guide", "difficulty": "Easy"},
    {"level": "Beginner", "subject": "English", "material_type": "Reading", "resource_name": "Simple Story Collection", "difficulty": "Easy"},
    {"level": "Beginner", "subject": "English", "material_type": "Vocabulary", "resource_name": "First 100 Words Pictionary", "difficulty": "Easy"},
    
    # Intermediate Level Materials
    {"level": "Intermediate", "subject": "Math", "material_type": "Algebra", "resource_name": "Algebra Foundations Textbook", "difficulty": "Medium"},
    {"level": "Intermediate", "subject": "Math", "material_type": "Geometry", "resource_name": "Shape and Space Workbook", "difficulty": "Medium"},
    {"level": "Intermediate", "subject": "English", "material_type": "Grammar", "resource_name": "Intermediate Grammar Rules Guide", "difficulty": "Medium"},
    {"level": "Intermediate", "subject": "English", "material_type": "Comprehension", "resource_name": "Reading Comprehension Passages", "difficulty": "Medium"},
    
    # Advanced Level Materials
    {"level": "Advanced", "subject": "Math", "material_type": "Trigonometry", "resource_name": "Advanced Trigonometry Textbook", "difficulty": "Hard"},
    {"level": "Advanced", "subject": "Math", "material_type": "Calculus", "resource_name": "Calculus Concepts and Applications", "difficulty": "Hard"},
    {"level": "Advanced", "subject": "English", "material_type": "Essay Writing", "resource_name": "Advanced Writing Techniques Guide", "difficulty": "Hard"},
    {"level": "Advanced", "subject": "English", "material_type": "Literature Analysis", "resource_name": "Critical Reading and Analysis Workbook", "difficulty": "Hard"}
]

# Convert to DataFrame
df = pd.DataFrame(study_materials)

# Save to CSV
df.to_csv('study_materials_database.csv', index=False)

# Function to get recommendations based on level
def get_study_materials(level):
    """
    Retrieve study materials for a specific learning level
    
    Args:
    level (str): Learning level (Beginner/Intermediate/Advanced)
    
    Returns:
    DataFrame: Recommended study materials
    """
    return df[df['level'] == level]

# Example usage
if __name__ == "__main__":
    # Demonstrate getting materials for different levels
    print("Beginner Level Materials:")
    print(get_study_materials("Beginner"))
    
    print("\nIntermediate Level Materials:")
    print(get_study_materials("Intermediate"))
    
    print("\nAdvanced Level Materials:")
    print(get_study_materials("Advanced"))
