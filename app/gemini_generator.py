import google.generativeai as genai
import os

# Configure with your Gemini API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)


def generate_workout_plan(name: str, age: int, gender: str, weight: str,
                          height: str, goal: str, fitness_level: str) -> str:
    """Generate a personalized workout plan using Gemini Pro."""
    prompt = f"""
    Create a detailed, personalized weekly workout plan for the following user:

    Name: {name}
    Age: {age}
    Gender: {gender}
    Weight: {weight}
    Height: {height}
    Fitness Goal: {goal}
    Fitness Level: {fitness_level}

    Please include:
    1. A 7-day workout schedule
    2. Specific exercises with sets and reps
    3. Rest day recommendations
    4. Warm-up and cool-down suggestions
    5. Safety tips based on their fitness level

    Format the plan in a clear, easy-to-follow structure with HTML formatting
    (use <h3>, <ul>, <li>, <strong>, <p> tags for readability).
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"<p>Error generating workout plan: {e}</p>"
