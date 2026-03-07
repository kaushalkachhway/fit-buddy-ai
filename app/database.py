from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped, mapped_column

# Base setup
Base = declarative_base()
engine = create_engine("sqlite:///fitness.db", echo=True)
SessionLocal = sessionmaker(bind=engine)


# User model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    goal: Mapped[str] = mapped_column(String, nullable=False)
    intensity: Mapped[str] = mapped_column(String, nullable=False)
    schedule: Mapped[int] = mapped_column(Integer, default=7)

    plans = relationship("WorkoutPlan", back_populates="user")


# WorkoutPlan model
class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    original_plan: Mapped[str] = mapped_column(Text, nullable=False)
    updated_plan: Mapped[str] = mapped_column(Text, nullable=True)  # feedback-based updates

    user = relationship("User", back_populates="plans")


# Create tables
Base.metadata.create_all(bind=engine)


# Save or update user info
def save_user(user_id: int, name: str, age: int, weight: float, goal: str, intensity: str):
    db = SessionLocal()
    existing = db.query(User).filter_by(id=user_id).first()
    if existing:
        existing.name = name
        existing.age = age
        existing.weight = weight
        existing.goal = goal
        existing.intensity = intensity
    else:
        user = User(
            id=user_id,
            name=name,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity,
            schedule=7
        )
        db.add(user)
    db.commit()
    db.close()


# Save original plan
def save_plan(user_id: int, plan: str):
    db = SessionLocal()
    workout = WorkoutPlan(user_id=user_id, original_plan=plan)
    db.add(workout)
    db.commit()
    db.close()


# Update plan with feedback
def update_plan(user_id: int, updated_text: str):
    db = SessionLocal()
    workout = db.query(WorkoutPlan).filter_by(user_id=user_id).order_by(WorkoutPlan.id.desc()).first()
    if workout:
        workout.updated_plan = updated_text
        db.commit()
    db.close()


# Get original plan
def get_original_plan(user_id: int):
    db = SessionLocal()
    workout = db.query(WorkoutPlan).filter_by(user_id=user_id).order_by(WorkoutPlan.id.desc()).first()
    db.close()
    return workout.original_plan if workout else None


# Get user info
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter_by(id=user_id).first()
    db.close()
    return user
