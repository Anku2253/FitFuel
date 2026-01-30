from fastapi import APIRouter
from schemas.workout import WorkoutPlan   # ← THIS WAS MISSING
from services.workout_service import generate_workout_plan

router = APIRouter()

@router.get("/plan", response_model=WorkoutPlan)
def workout_plan(bmi: float):
    intensity, exercises = generate_workout_plan(bmi)
    return {
        "intensity": intensity,
        "exercises": exercises
    }