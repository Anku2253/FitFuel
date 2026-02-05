import random

def generate_meal_plan(request):
    breakfast = [
        {"name": "Oats", "calories": 250},
        {"name": "Banana", "calories": 100}
    ]

    lunch = [
        {"name": "Rice", "calories": 300},
        {"name": "Dal", "calories": 200}
    ]

    dinner = [
        {"name": "Roti", "calories": 250},
        {"name": "Sabzi", "calories": 150}
    ]

    total = sum(item["calories"] for item in breakfast + lunch + dinner)

    return {
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,
        "total_calories": total
    }


def get_daily_tip():
    tips = [
        "Drink at least 3 liters of water today",
        "Walk 10,000 steps",
        "Avoid sugar after 7 PM",
        "Eat protein in every meal"
    ]
    return {"tip": random.choice(tips)}
