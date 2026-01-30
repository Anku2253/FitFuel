from fastapi import APIRouter
from schemas.nutrition import NutritionPlan
from services.nutrition_service import generate_nutrition_plan

router = APIRouter()

@router.get("/ping", response_model=NutritionPlan)
def get_nutrition_plan(bmi: float, goal: str):
    calories, meals = generate_nutrition_plan(bmi, goal)
    return {
        "calorie_target": calories,
        "meals": meals
    }
