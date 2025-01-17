import os
from typing import Any

from dotenv import load_dotenv

from polymath.config.types import EnvironmentConfig


class EnvConfigStore:
    def load(self) -> Any:
        return {
            key.lower(): value for key, value in os.environ.items()
        }


class EnvConfigLoader:
    def __init__(self):
        load_dotenv()

    def load_environment_config(self) -> EnvironmentConfig:
        config = EnvConfigStore().load()
        return EnvironmentConfig(config)


Env = EnvConfigLoader()
