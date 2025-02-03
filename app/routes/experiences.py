from fastapi import APIRouter, Depends, Security
from app.routes import experiences
from sqlalchemy.orm import Session
from database.database import get_db
from database.schemas import ExperienceCreate 
from app.services.experience import log_experience

router = APIRouter(prefix="/experiences")

@router.get("/")
async def find_experiences(
):
    return {"message": "hello"}

@router.post("/")
async def create_experience(experience_data: ExperienceCreate, db: Session = Depends(get_db)):
    return await log_experience(experience_data, db)