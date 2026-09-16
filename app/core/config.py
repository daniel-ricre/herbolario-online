from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Herbolario Online"
    app_env: str = "development"
    debug: bool = True

    database_url: str = "sqlite+aiosqlite:///./herbolario.db"

    secret_key: str = "dev-secret-key-change-me"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
