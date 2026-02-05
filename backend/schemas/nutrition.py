from pydantic import BaseModel
from typing import List

class MealPlanRequest(BaseModel):
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    activity_level: str
    goal: str   # lose | maintain | gain

class MealItem(BaseModel):
    name: str
    calories: int

class MealPlanResponse(BaseModel):
    breakfast: List[MealItem]
    lunch: List[MealItem]
    dinner: List[MealItem]
    total_calories: int

class DailyTipResponse(BaseModel):
    tip: str
