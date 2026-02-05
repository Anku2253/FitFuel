from fastapi import APIRouter
from schemas.nutrition import (
    MealPlanRequest,
    MealPlanResponse,
    DailyTipResponse
)
from services.nutrition_service import (
    generate_meal_plan,
    get_daily_tip
)

router = APIRouter(prefix="/nutrition", tags=["Nutrition"])

@router.post("/meal-plan", response_model=MealPlanResponse)
def meal_plan(request: MealPlanRequest):
    return generate_meal_plan(request)

@router.get("/daily-tips", response_model=DailyTipResponse)
def daily_tips():
    return get_daily_tip()
