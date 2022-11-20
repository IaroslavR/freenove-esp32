"""CLI tool."""

from loguru import logger as log
import typer

from .helpers.cfg import log_config

cli = typer.Typer()
log.configure(**log_config)


@cli.command()
@log.catch
def hello(name: str) -> str:
    """Hello command."""
    log.info("Started", command="hello")
    message = f"Hello {name}111"
    log.success(message)
    return message


@cli.command()
@log.catch
def ciao(name: str) -> str:
    """Chao command."""
    log.info("Started", command="ciao")
    message = f"Ciao {name}"
    log.success(message)
    return message


if __name__ == "__main__":
    cli()
