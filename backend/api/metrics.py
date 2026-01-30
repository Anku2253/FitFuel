from fastapi import APIRouter
from schemas.metrics import MetricsInput, MetricsOutput
from services.bmi_service import calculate_bmi, classify_bmi
from services.body_fat_service import calculate_body_fat, classify_body_fat

router = APIRouter()

@router.post("/calculate", response_model=MetricsOutput)
def calculate_metrics(data: MetricsInput):
    print("Received : ",data)
    bmi = calculate_bmi(data.height_cm, data.weight_kg)
    bmi_category = classify_bmi(bmi)

    body_fat = calculate_body_fat(
        bmi=bmi,
        age=data.age,
        gender=data.gender
    )
    body_fat_category = classify_body_fat(
        body_fat,
        data.gender
    )

    return MetricsOutput(
        bmi=bmi,
        bmi_category=bmi_category,
        body_fat_percentage=body_fat,
        body_fat_category=body_fat_category
    )
