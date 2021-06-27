from sqlalchemy import create_engine
from .config  import AppConfig

config = AppConfig()

engine = create_engine(config.db_connection_string, connect_args={"check_same_thread": False})