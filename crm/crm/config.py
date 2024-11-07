from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class UsersSettings(BaseSettings):
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    OPERATOR_USERNAME: str
    OPERATOR_PASSWORD: str
    MARKETER_USERNAME: str
    MARKETER_PASSWORD: str
    MANAGER_USERNAME: str
    MANAGER_PASSWORD: str


class DBSettings(BaseSettings):
    """
    Класс для настройки параметров подключения к базе данных.
    """

    HOST: str
    PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def database_url(self) -> str:
        """
        Возвращает строку для подключения к базе данных.
        """
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.HOST}:{self.PORT}/{self.POSTGRES_DB}"
        )


class RedisSettings(BaseSettings):
    REDIS_HOST: str

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:6379/0"


class Settings(BaseSettings):
    """
    Класс с настройками телеграма, api и базы данных
    """

    DB: DBSettings = DBSettings()
    REDIS: RedisSettings = RedisSettings()
    USERS: UsersSettings = UsersSettings()


config = Settings()
