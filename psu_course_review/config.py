from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SQLDB_URL: str
    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 * 60  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60  # 7 days

    model_config = SettingsConfigDict(
        env_file=".env", validate_assignment=True, extra="allow"
    )


def get_settings():
    return Settings()