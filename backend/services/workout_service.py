def generate_workout_plan(bmi: float):
    if bmi >= 25:
        return "Low", ["Walking", "Bodyweight Squats"]
    return "Moderate", ["Jogging", "Push-ups"]
