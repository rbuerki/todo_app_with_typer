"""This module provides the ToDo database functionality."""

import configparser
import json
from pathlib import Path
from typing import Any, NamedTuple

from todo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

# Default path in case the user does not provide a json file path
DEFAULT_DB_FILE_PATH = Path(__file__).parent.parent / "default_todo.json"


class DBResponse(NamedTuple):
    todo_list: list[dict[str, Any]]
    error: int


class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read_todos(self) -> DBResponse:
        """Read the todos from the database."""
        try:
            with self._db_path.open("r") as db_file:
                try:
                    return DBResponse(json.load(db_file), SUCCESS)
                except json.JSONDecodeError:
                    return DBResponse([], JSON_ERROR)
        except OSError:
            return DBResponse([], DB_READ_ERROR)

    def write_todos(self, todo_list: list[dict[str, Any]]) -> DBResponse:
        try:
            with self._db_path.open("w") as db_file:
                json.dump(todo_list, db_file, indent=4)
                return DBResponse(todo_list, SUCCESS)
        except OSError:
            return DBResponse(todo_list, DB_WRITE_ERROR)


def get_database_path(config_file: Path) -> Path:
    """Return the path to the database file."""
    config = configparser.ConfigParser()
    config.read(config_file)
    return Path(config["General"]["database"])


def init_database(db_path: Path) -> int:
    """Initialize the database."""
    try:
        db_path.write_text("[]")  # Initializes empty ToDo list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
