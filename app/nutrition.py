from app.gemini_flash_generator import generate_nutrition_tip


def get_nutrition_advice(goal: str, weight: str, fitness_level: str) -> str:
    """Wrapper for nutrition-specific logic."""
    return generate_nutrition_tip(goal, weight, fitness_level)
