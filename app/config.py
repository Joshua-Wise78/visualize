from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the codebase enviornment"""

    environment: str = "dev"
    allowed_hosts: str = "localhost,127.0.0.1"

    class Config:
        env_file = ".env"


settings = Settings()
