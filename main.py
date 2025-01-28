from fastapi import FastAPI
from app.routes import experiences

app = FastAPI()

app.include_router(experiences.router)