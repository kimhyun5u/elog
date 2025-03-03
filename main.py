from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import experiences, home
from database.database import engine
from database import models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home.router)
app.include_router(experiences.router)

models.Base.metadata.create_all(bind=engine)
