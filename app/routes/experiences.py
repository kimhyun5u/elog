from fastapi import APIRouter, Depends, Security
from app.routes import experiences
from sqlalchemy.orm import Session
from database.database import get_db
from database import models, schemas

router = APIRouter(prefix="/experiences")

@router.get("/")
async def find_experiences(
):
    return {"message": "hello"}

@router.post("/")
async def create_experience(
db: Session = Depends(get_db)):
    new_experience = models.Experience(
        title="new experience",
        start_date="2021-01-01",
        end_date="2021-12-31",
        description="new description"
    )
    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)
    return new_experience