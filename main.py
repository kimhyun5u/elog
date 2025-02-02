from fastapi import FastAPI
from app.routes import experiences, home
from database.database import engine
from database import models

app = FastAPI()

app.include_router(home.router)
app.include_router(experiences.router)

models.Base.metadata.create_all(bind=engine)
