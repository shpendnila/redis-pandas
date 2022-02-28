import logging


def get_logger(log_level=logging.INFO, log_format: str = None) -> logging.Logger:
    if not log_format:
        log_format = (
            "%(asctime)s - %(levelname)s - %(message)s -%(lineno)s : %(threadName)s"
        )
    logging.basicConfig(level=log_level, format=log_format)
    return logging.getLogger(__name__)
