from pydantic import BaseModel
from typing import List

class MealItem(BaseModel):
    food: str
    portion_g: int
    reason: str

class NutritionPlan(BaseModel):
    calorie_target: int
    meals: List[MealItem]
