from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "TASK_2"
    DATABASE_URL: str | None = "sqlite+aiosqlite:///./users_database.db"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
