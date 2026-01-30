from pydantic import BaseModel
from typing import List

class WorkoutPlan(BaseModel):
    intensity: str
    exercises: List[str]
