from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8040

    IMEICHECK_API_SANDBOX_TOKEN: str

    BOT_TOKEN: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
WHITELIST: list[int] = [173809062, ]
