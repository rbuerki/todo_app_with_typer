"""This module provides the command line interface for the todo app."""

from typing import Optional
import typer
from pathlib import Path
from typing_extensions import Annotated
from todo import ERRORS, __app_name__, __version__, config, database


app = typer.Typer()


@app.command()
def init(
    db_path: Annotated[
        str,
        typer.Option(
            "--db-path",
            "-db",
            prompt="Enter Todo database location or press enter to use default",
        ),
    ] = str(database.DEFAULT_DB_FILE_PATH)
) -> None:
    """Initialize the database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f"Creating config file failed with {ERRORS[app_init_error]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    db_init_error = database.init_database(Path(db_path))
    if app_init_error:
        typer.secho(
            f"Creating database file failed with {ERRORS[db_init_error]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    else:
        typer.secho(
            f"Database initialized successfully at {db_path}.",
            fg=typer.colors.GREEN,
        )


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
