from pydantic import BaseModel

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
    start_date: str
    end_date: str
    description: str

class ExperienceCreate(ExperienceBase):
    pass

class Experience(ExperienceBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy 모델을 Pydantic 모델로 변환 가능하게 함