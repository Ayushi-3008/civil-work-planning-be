# common/logger.py

import logging
import json
from datetime import datetime


class JSONFormatter(logging.Formatter):
    """
    Custom JSON formatter for structured logging.
    Suitable for production, microservices, ELK, Datadog, etc.
    """

    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }

        # include stack trace (error traceback)
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_data)


def get_logger(name="app"):
    """
    Returns a logger with JSON formatting.

    Used across the project:
    logger = get_logger(__name__)
    logger.info("something")
    """

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        handler.setFormatter(JSONFormatter())

        logger.addHandler(handler)

    return logger


# Global reusable logger instance
logger = get_logger("global")