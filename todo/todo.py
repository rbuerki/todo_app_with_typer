"""This module provides the model-controller."""

from typing import Any, NamedTuple
from pathlib import Path

from todo.database import DatabaseHandler


class CurentToDo(NamedTuple):
    """A named tuple to store the current todo."""
    todo: dict[str, Any]
    error: int


class Todoer:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)
