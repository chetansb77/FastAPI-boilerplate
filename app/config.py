from logging import debug
import os
from decouple import config


class AppConfig:
    connection_string: str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + config('SERVER') + ";Database=" + config(
        'DATABASE_NAME') + ";UID=" + config('DBUSER') + ";PWD=" + config('DBPWD') + ";Mars_Connection=Yes"

app_config = AppConfig()