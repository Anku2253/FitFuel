from pydantic import BaseModel


class HydrationInput(BaseModel):
    weight_kg: float
    activity_level: str


class HydrationOutput(BaseModel):
    daily_water_liters: float
    message: str
