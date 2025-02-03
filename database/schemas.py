from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy 모델을 Pydantic 모델로 변환 가능하게 함

class ExperienceBase(BaseModel):
    title: str
    start_date: date
    end_date: date
    description: str

class ExperienceCreate(ExperienceBase):
    title: str
    start_date: date
    end_date: date
    description: str

class Experience(ExperienceBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy 모델을 Pydantic 모델로 변환 가능하게 함