from database import models, schemas
from sqlalchemy.orm import Session


async def log_experience(experience_data: schemas.ExperienceCreate, db: Session):
    new_experience = models.Experience(
        title=experience_data.title,
        start_date=experience_data.start_date,
        end_date=experience_data.end_date,
        description=experience_data.description
    )
    
    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)

    return new_experience