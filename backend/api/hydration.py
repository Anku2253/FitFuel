from fastapi import APIRouter
from services.hydration_service import calculate_water
from schemas.hydration import HydrationInput, HydrationOutput

router = APIRouter()

@router.get("/target")
def hydration_target(weight_kg: float):
    return {"liters_per_day": calculate_water(weight_kg)}

