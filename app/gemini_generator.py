import google.generativeai as genai
import os
from typing import Dict, Any

# Configure with your Gemini API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-lite")


def generate_workout_gemini(user_input: Dict[str, Any]) -> str:
    """
    Generate a personalized 7-day workout plan using Gemini.

    Args:
        user_input: Dictionary containing 'goal' and 'intensity' keys

    Returns:
        Formatted 7-day workout plan as a string
    """
    goal = user_input.get("goal", "General Fitness")
    intensity = user_input.get("intensity", "Medium").lower()

    # Validate and normalize intensity
    valid_intensities = ["low", "medium", "high"]
    if intensity not in valid_intensities:
        intensity = "medium"

    # Create a structured prompt for consistent output
    prompt = f"""You are a certified professional fitness trainer with 10+ years of experience.

Create a highly detailed, personalized 7-day workout plan for a client with the following profile:
- Goal: {goal}
- Intensity Level: {intensity}

IMPORTANT: Format the response EXACTLY as follows for each day:

Day 1: [Day Name/Focus Area]
Warm-up (5-10 mins):
[Specific warm-up exercises with duration]

Main Workout:
[Exercise 1: Sets x Reps, Notes]
[Exercise 2: Sets x Reps, Notes]
[Exercise 3: Sets x Reps, Notes]
[Add more exercises as appropriate]

Cooldown / Recovery Tip:
[Specific cooldown routine or recovery strategy]

---

Repeat this format for Day 2 through Day 7.

Guidelines:
1. Each warm-up should be 5-10 minutes and appropriate for the day's focus
2. Main workout should include 4-6 exercises with specific sets and reps
3. All exercises should align with the goal: {goal}
4. Intensity should be: {intensity}
5. Include rest days or active recovery days as appropriate
6. Provide realistic, achievable progressions
7. Include safety notes where applicable
8. Make exercises adaptable for home or gym settings

Start generating the 7-day plan now:"""

    try:
        response = model.generate_content(prompt)

        if not response or not response.text:
            return "Error: No response from Gemini API"

        # Parse and format the response for better readability
        plan_text = response.text.strip()

        # Add styling markers for frontend rendering
        formatted_plan = _format_workout_plan(plan_text)

        return formatted_plan

    except Exception as e:
        return f"Error generating workout plan: {str(e)}"


def _format_workout_plan(plan_text: str) -> str:
    """
    Format the raw workout plan text for better readability.

    Args:
        plan_text: Raw text response from Gemini

    Returns:
        Formatted workout plan
    """
    lines = plan_text.split('\n')
    formatted_lines = []

    for line in lines:
        if line.strip().startswith('Day ') and ':' in line:
            formatted_lines.append(f"\n{'='*60}")
            formatted_lines.append(line.strip())
            formatted_lines.append('='*60)
        elif line.strip().startswith(('Warm-up', 'Main Workout', 'Cooldown')):
            formatted_lines.append(f"\n► {line.strip()}")
        else:
            formatted_lines.append(line)

    return '\n'.join(formatted_lines)


def validate_workout_input(goal: str, intensity: str) -> tuple[bool, str]:
    """
    Validate user input for workout plan generation.

    Args:
        goal: User's fitness goal
        intensity: Workout intensity level

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not goal or not goal.strip():
        return False, "Fitness goal is required"

    valid_intensities = ["low", "medium", "high"]
    if intensity.lower() not in valid_intensities:
        return False, f"Intensity must be one of: {', '.join(valid_intensities)}"

    if len(goal) > 200:
        return False, "Fitness goal description is too long (max 200 characters)"

    return True, ""
