# study_materials.py
def get_study_materials():
    """
    Returns a dictionary of study materials organized by subject and level.
    """
    return {
        "Mathematics": {
            "beginner": [
                {"title": "Basic Arithmetic", "url": "https://example.com/basic-math", "description": "Learn addition, subtraction, multiplication and division"},
                {"title": "Introduction to Fractions", "url": "https://example.com/fractions", "description": "Understanding fractions and their operations"}
            ],
            "intermediate": [
                {"title": "Algebra Fundamentals", "url": "https://example.com/algebra", "description": "Learn equations, variables and expressions"},
                {"title": "Geometry Basics", "url": "https://example.com/geometry", "description": "Understand shapes, angles and theorems"}
            ],
            "advanced": [
                {"title": "Trigonometry", "url": "https://example.com/trigonometry", "description": "Master sine, cosine and tangent"},
                {"title": "Calculus Introduction", "url": "https://example.com/calculus", "description": "Learn derivatives and integrals"}
            ]
        },
        "Science": {
            "beginner": [
                {"title": "Basic Science Concepts", "url": "https://example.com/basic-science", "description": "Introduction to scientific method and basic concepts"},
                {"title": "Plants and Animals", "url": "https://example.com/biology-intro", "description": "Learn about living organisms"}
            ],
            "intermediate": [
                {"title": "Physics Fundamentals", "url": "https://example.com/physics", "description": "Learn about motion, forces and energy"},
                {"title": "Chemistry Basics", "url": "https://example.com/chemistry", "description": "Understand elements, compounds and reactions"}
            ],
            "advanced": [
                {"title": "Advanced Biology", "url": "https://example.com/adv-biology", "description": "Study genetics, evolution and cellular biology"},
                {"title": "Quantum Physics", "url": "https://example.com/quantum", "description": "Explore particle physics and quantum mechanics"}
            ]
        }
    }