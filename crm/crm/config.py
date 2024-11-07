from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


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


class Settings(BaseSettings):
    """
    Класс с настройками телеграма, api и базы данных
    """

    DB: DBSettings = DBSettings()


config = Settings()
