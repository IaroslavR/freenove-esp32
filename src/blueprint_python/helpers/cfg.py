"""CLI configuration."""
import os
import sys

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "SUCCESS")
FILE_LOGGING_LEVEL = os.getenv("FILE_LOGGING_LEVEL", LOGGING_LEVEL)
FILE_LOGGING_SIZE = "1 MB"


log_config = {
    "handlers": [
        {
            "colorize": True,
            "format": "{time} <level>{message}</level> | {extra}",
            "level": LOGGING_LEVEL,
            "sink": sys.stdout,
        },
        {
            "format": "{message}",
            "level": FILE_LOGGING_LEVEL,
            "rotation": FILE_LOGGING_SIZE,
            "serialize": True,
            "sink": "cli-log.jsonl",
        },
    ],
}
