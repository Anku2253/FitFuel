def generate_nutrition_plan(bmi: float, goal: str):
    if goal == "lose":
        calories = 1800
    elif goal == "gain":
        calories = 2600
    else:
        calories = 2200

    meals = [
        {
            "food": "Roti",
            "portion_g": 100,
            "reason": "Complex carbs for sustained energy"
        },
        {
            "food": "Dal",
            "portion_g": 150,
            "reason": "Plant protein source"
        },
        {
            "food": "Curd",
            "portion_g": 100,
            "reason": "Gut health and calcium"
        }
    ]

    return calories, meals
