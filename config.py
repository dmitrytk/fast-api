from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = "Fast App"
    postgres_password: str

    class Config:
        env_file = ".env"
