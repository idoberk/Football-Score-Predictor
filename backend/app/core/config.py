"""Application configuration using Pydantic Settings"""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # App Configuration
    APP_NAME: str = "Football Predictor API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    API_VERSION: str = "v1"
    
    # Database Configuration
    DATABASE_URL: str = "postgresql://localhost/football_predictor"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_ECHO: bool = False
    
    # External API Configuration
    FOOTBALL_API_KEY: str = ""
    FOOTBALL_API_BASE_URL: str = "https://api-football-v1.p.rapidapi.com/v3"
    REAL_MADRID_TEAM_ID: int = 541
    EXTERNAL_API_TIMEOUT: int = 10
    EXTERNAL_API_MAX_RETRIES: int = 3
    
    # ML Configuration
    MODEL_PATH: str = "models/prediction_model.pkl"
    MIN_TRAINING_SAMPLES: int = 100
    RETRAIN_THRESHOLD_ACCURACY: float = 0.50
    
    # Security Configuration
    API_KEY_HEADER: str = "X-API-Key"
    RATE_LIMIT_PER_MINUTE: int = 100
    ALLOWED_ORIGINS: list[str] = ["*"]
    
    # Cache Configuration
    REDIS_URL: Optional[str] = None
    CACHE_TTL_SECONDS: int = 300
    PREDICTION_CACHE_TTL: int = 300  # 5 minutes
    MATCH_CACHE_TTL: int = 3600  # 1 hour
    STATS_CACHE_TTL: int = 1800  # 30 minutes
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"  # json or text
    
    # Background Tasks Configuration
    SYNC_FIXTURES_INTERVAL_HOURS: int = 24
    UPDATE_RESULTS_INTERVAL_HOURS: int = 2
    RETRAIN_MODEL_INTERVAL_DAYS: int = 7
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
