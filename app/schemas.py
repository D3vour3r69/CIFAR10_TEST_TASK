from pydantic import BaseModel
from typing import Dict

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    all_probabilities: Dict[str, float]

class HealthResponse(BaseModel):
    status: str

class ClassesResponse(BaseModel):
    classes: list[str]

class ErrorResponse(BaseModel):
    detail: str