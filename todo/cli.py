"""This module provides the command line interface for the todo app."""

from typing import Optional
import typer
from typing_extensions import Annotated
from todo import ERRORS, __app_name__, __version__


app = typer.Typer()


def _version_callback(version: bool) -> None:
    if version:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            help="Print the version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
    ] = None
) -> None:
    """The main entry point for the todo app."""
    pass
