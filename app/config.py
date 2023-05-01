# External libraries
import os

from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Simple api'


@lru_cache()
def get_settings() -> Settings:
    return Settings()

