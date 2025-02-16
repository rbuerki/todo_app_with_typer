__app_name__ = "todo"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_WRITE_ERROR,
    DB_READ_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "Config directory Error",
    FILE_ERROR: "Config ile Error",
    DB_WRITE_ERROR: "Database Write Error",
    DB_READ_ERROR: "Database Read Error",
    JSON_ERROR: "JSON operation Error",
    ID_ERROR: "ToDo ID Error",
}
