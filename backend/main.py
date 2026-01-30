from fastapi import FastAPI
from api import metrics, nutrition, workout, hydration

app = FastAPI(
    title="FitFuel API",
    description="Rule-based fitness and nutrition engine",
    version="0.1.0"
)

app.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
app.include_router(nutrition.router, prefix="/nutrition", tags=["Nutrition"])
app.include_router(workout.router, prefix="/workout", tags=["Workout"])
app.include_router(hydration.router, prefix="/hydration", tags=["Hydration"])
