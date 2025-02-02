from fastapi import APIRouter
from app.routes import home

router = APIRouter(prefix="")

@router.get("/")
async def retrieve_home():
    return "home"