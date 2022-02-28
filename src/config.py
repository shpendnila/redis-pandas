from functools import lru_cache
import os


class Config(object):
    HOST = os.getenv("HOST", "localhost")
    PORT = os.getenv("PORT", 6379)
    LOG_LEVEL = int(os.getenv("LOG_LEVEL", 10))


@lru_cache
def get_config():
    return Config()


configuration: Config = get_config()
