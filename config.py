from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Auth System"
    SECRET_KEY: str = "your-secret-key-here"  # In production, use environment variable
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./sql_app.db"  # For development
    
    class Config:
        env_file = ".env"

settings = Settings()