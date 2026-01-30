from pydantic import BaseModel
from pydantic import ConfigDict

class MetricsInput(BaseModel):
    age: int
    gender: str
    height_cm: float
    weight_kg: float

    model_config = ConfigDict(extra="ignore")

class MetricsOutput(BaseModel):
    bmi: float
    bmi_category: str
    body_fat_percentage: float
    body_fat_category: str
