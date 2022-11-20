"""CLI tool."""
import sys

from loguru import logger as log
import typer

from .cfg import log_config

cli = typer.Typer()
log.configure(**log_config)


@cli.command()
@log.catch
def hello() -> str:
    """ESP32 connection check."""
    command = sys._getframe().f_code.co_name
    log.info("Started", command=command)
    return command


if __name__ == "__main__":
    cli()
