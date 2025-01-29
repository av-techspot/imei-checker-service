from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_host: str = "0.0.0.0"
    api_port: int = 8040

    imeicheck_api_sandbox_token: str

    bot_token: str

    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_name: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
