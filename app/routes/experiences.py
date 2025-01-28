from fastapi import APIRouter, Depends, Security
from app.routes import experiences

router = APIRouter(prefix="/experiences")

@router.get("/")
async def create_experience(
):
    return {"message": "hello"}