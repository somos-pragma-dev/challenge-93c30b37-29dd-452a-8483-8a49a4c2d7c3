from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    app_name: str = "Banking API"
    app_version: str = "1.0.0"
    debug: bool = False

    database_url: str = "sqlite+aiosqlite:///./banking.db"
    database_echo: bool = False
    database_pool_size: int = 20
    database_max_overflow: int = 10

    jwt_secret_key: str = "supersecretkeychangemeinproduction123456789"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7

    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:8000"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ["*"]
    cors_allow_headers: list[str] = ["*"]

    api_v1_prefix: str = "/api/v1"
    api_title: str = "Banking Account Management API"
    api_description: str = "API REST para gestión de cuentas bancarias"

    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    @property
    def is_production(self) -> bool:
        return not self.debug

    @property
    def database_pool_config(self) -> dict:
        return {
            "pool_size": self.database_pool_size,
            "max_overflow": self.database_max_overflow,
            "pool_pre_ping": True,
            "pool_recycle": 3600
        }


settings = Settings()


def get_settings() -> Settings:
    return settings