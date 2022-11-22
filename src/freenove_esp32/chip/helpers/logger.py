"""Configure logger."""
import ulogger

from helpers.cfg import FILE_LOGGING_LEVEL, LOGGING_LEVEL


handler = ulogger.Handler(
    level=getattr(ulogger, LOGGING_LEVEL),
)
file_handler = ulogger.Handler(
    level=getattr(ulogger, FILE_LOGGING_LEVEL),
    direction=ulogger.TO_FILE,
)


def get_logger(name: str) -> ulogger.Logger:
    """Get configured logger.

    Args:
        name: logger name

    Returns:
        ulogger instance
    """
    return ulogger.Logger(name=name, handlers=[handler, file_handler])
