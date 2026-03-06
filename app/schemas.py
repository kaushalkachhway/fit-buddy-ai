from pydantic import BaseModel, Field


class UserInput(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=10, le=100)
    gender: str = Field(..., min_length=1, max_length=20)
    weight: str = Field(..., min_length=1, max_length=20)
    height: str = Field(..., min_length=1, max_length=20)
    goal: str = Field(..., min_length=1, max_length=100)
    intensity: str = Field(..., min_length=1, max_length=20)
    fitness_level: str = Field(..., min_length=1, max_length=50)


class FeedbackInput(BaseModel):
    user_id: int
    feedback: str = Field(..., min_length=1, max_length=1000)
