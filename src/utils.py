from src.config import configuration
from src.logger import get_logger

import redis
import pandas as pd
import pyarrow as pa


logger = get_logger(log_level=configuration.LOG_LEVEL)


def get_redis_client():
    return redis.Redis(
        host=configuration.HOST,
        port=configuration.PORT
    )


def create_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {"a_column": ['1', '2', '3']}
    )


def store_in_redis(key: str, a_df: pd.DataFrame, redis_client):
    df_compressed = pa.serialize(a_df).to_buffer().to_pybytes()
    res = redis_client.set(key, df_compressed)
    if res:
        logger.info(f'{key} cached')


def load_from_redis(key: str, redis_client) -> pd.DataFrame:
    data = redis_client.get(key)
    try:
        return pa.deserialize(data)
    except Exception as e:
        logger.error("No data")
        logger.error(e)
