from decouple import config


class AppConfig:

    def __init__(self) -> None:
        self.db_connection_string = config('SQLLITE_CONNECTION_STRING')


class PostgreSQLConfig(AppConfig):

    def __init__(self) -> None:
        super().__init__()
        self.db_connection_string = config('POSTGRESQL_CONNECTION_STRING')
