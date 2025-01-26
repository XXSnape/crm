from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class UsersSettings(BaseSettings):
    """
    Класс для настройки данных о пользователях
    """

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
    """Класс для настройки редиса"""

    REDIS_HOST: str

    @property
    def redis_url(self) -> str:
        """
        Возвращает строку для подключения к редису
        :return:
        """
        return f"redis://{self.REDIS_HOST}:6379/0"


class Settings(BaseSettings):
    """
    Класс с настройками базы данных, редиса и пользователей
    """

    DB: DBSettings = DBSettings()
    REDIS: RedisSettings = RedisSettings()
    USERS: UsersSettings = UsersSettings()


config = Settings()
