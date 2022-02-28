from src.config import configuration
from src.logger import get_logger
from utils import (
    get_redis_client,
    create_dataframe,
    store_in_redis,
    load_from_redis
)

logger = get_logger(log_level=configuration.LOG_LEVEL)


def main():
    df_key = "test_dataframe"
    redis_client = get_redis_client()
    df = create_dataframe()

    logger.info(f"DataFrame:\n{df}\nwill be stored with the key {df_key}")

    store_in_redis(
        df_key,
        df,
        redis_client,
    )

    stored_df = load_from_redis(
        df_key,
        redis_client,
    )

    logger.info(stored_df)


if __name__ == '__main__':
    main()
