from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str

    port: int = 8000

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()