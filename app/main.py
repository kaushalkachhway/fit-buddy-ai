import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import init_db
from app.routes import router

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="FitBuddy AI", description="AI-Powered Fitness Plan Generator")

# Mount static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Include routes
app.include_router(router)


@app.on_event("startup")
def on_startup():
    """Initialize the database on server startup."""
    init_db()
