"""This module provides the config functionality for the todo app."""

import configparser
from pathlib import Path
import typer

from todo import(
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    DIR_ERROR,
    FILE_ERROR,
    SUCCESS,
    __app_name__,
)

CONFIG_DIR_PATH = Path(__file__).parent.parent
CONFIG_FLIE_PATH = CONFIG_DIR_PATH / "config.ini"


def init_app(db_path: str) -> int:
    """Initialize the app."""
    result = _init_config_file()
    if result != SUCCESS:
        return result

    result = _create_database(db_path)
    if result != SUCCESS:
        return result

    return SUCCESS


def _init_config_file() -> int:
    """Create the config file."""
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR

    try:
        CONFIG_FLIE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR

    return SUCCESS


def _create_database(db_path: str) -> int:
    """Create the database."""
    config = configparser.ConfigParser()
    config["General"] = {"database": db_path}

    try:
        with CONFIG_FLIE_PATH.open("w") as f:
            config.write(f)
    except OSError:
        return DB_WRITE_ERROR

    return SUCCESS
