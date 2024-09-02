import os

from pydantic import SecretStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    token: SecretStr = os.getenv("BOT_TOKEN")
    web_app_url: SecretStr = os.getenv("WEB_APP_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
