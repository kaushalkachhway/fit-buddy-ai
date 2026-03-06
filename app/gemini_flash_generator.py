import google.generativeai as genai
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)


def generate_nutrition_tip(goal: str, weight: str, fitness_level: str) -> str:
    """Generate a nutrition tip using Gemini Flash."""
    prompt = f"""
    Provide a concise, personalized nutrition tip for someone with the following profile:

    Fitness Goal: {goal}
    Weight: {weight}
    Fitness Level: {fitness_level}

    Include:
    1. A quick daily nutrition tip
    2. Foods to prioritize
    3. Foods to avoid
    4. Hydration advice

    Format with HTML tags (<h3>, <ul>, <li>, <strong>, <p>) for readability.
    Keep it brief and actionable.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"<p>Error generating nutrition tip: {e}</p>"
