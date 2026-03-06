import google.generativeai as genai
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)


def update_plan_with_feedback(original_plan: str, feedback: str) -> str:
    """Update a workout plan based on user feedback using Gemini."""
    prompt = f"""
    The user has the following workout plan:

    {original_plan}

    They provided this feedback:
    "{feedback}"

    Please update and improve the workout plan based on their feedback.
    Keep the same HTML formatting style (<h3>, <ul>, <li>, <strong>, <p> tags).
    Make the adjustments practical and safe.
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"<p>Error updating plan: {e}</p>"
