from pydantic import BaseSettings


class Settings(BaseSettings):
    EMAIL: str
    EMAIL_PASSWORD: str
    EMAIL_HOST: str
    EMAIL_PORT: int
    RABBIT_USERNAME: str
    RABBIT_PASSWORD: str
    RABBIT_HOST: str
    RABBIT_VHOST: str

    class Config:
        env_file = './.env'


settings = Settings()
