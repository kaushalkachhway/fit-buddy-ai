from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pathlib import Path

from app.database import get_db, User
from app.gemini_generator import generate_workout_plan
from app.gemini_flash_generator import generate_nutrition_tip
from app.updated_plan import update_plan_with_feedback

BASE_DIR = Path(__file__).resolve().parent.parent

router = APIRouter()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the user input form."""
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/generate", response_class=HTMLResponse)
async def generate_plan(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    weight: str = Form(...),
    height: str = Form(...),
    goal: str = Form(...),
    fitness_level: str = Form(...),
    db: Session = Depends(get_db),
):
    """Generate workout plan and nutrition tip, save user to DB."""
    # Generate AI content
    workout_plan = generate_workout_plan(name, age, gender, weight, height, goal, fitness_level)
    nutrition_tip = generate_nutrition_tip(goal, weight, fitness_level)

    # Save to database
    user = User(
        name=name,
        age=age,
        gender=gender,
        weight=weight,
        height=height,
        goal=goal,
        fitness_level=fitness_level,
        workout_plan=workout_plan,
        nutrition_tip=nutrition_tip,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "user": user,
            "workout_plan": workout_plan,
            "nutrition_tip": nutrition_tip,
        },
    )


@router.post("/feedback", response_class=HTMLResponse)
async def submit_feedback(
    request: Request,
    user_id: int = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db),
):
    """Process user feedback and update the workout plan."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return templates.TemplateResponse(
            "index.html", {"request": request, "error": "User not found."}
        )

    # Update plan based on feedback
    updated_plan = update_plan_with_feedback(user.workout_plan or "", feedback)
    user.workout_plan = updated_plan
    user.feedback = feedback
    db.commit()
    db.refresh(user)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "user": user,
            "workout_plan": updated_plan,
            "nutrition_tip": user.nutrition_tip,
            "feedback_msg": "Your plan has been updated based on your feedback!",
        },
    )


@router.get("/admin/users", response_class=HTMLResponse)
async def all_users(request: Request, db: Session = Depends(get_db)):
    """Admin dashboard — list all users."""
    users = db.query(User).order_by(User.created_at.desc()).all()
    return templates.TemplateResponse(
        "all_users.html", {"request": request, "users": users}
    )
