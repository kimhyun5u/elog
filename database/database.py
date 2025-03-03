from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

# MySQL 연결 URL 설정

# SQLAlchemy 엔진 생성
engine = create_engine(settings.db_url, echo=True)

# 세션 생성기 설정
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델 생성을 위한 Base 클래스
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()