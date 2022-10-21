import pandas as pd
import pyodbc
import json
import os
from ..config import app_config

# TODO: Add docstrings
class Accessor:
    def __init__(self):
        self.db_configuration = app_config
        self.cnxn = pyodbc.connect(
            self.db_configuration.connection_string, autocommit=True)
        self.cursor = self.cnxn.cursor()
        self.cursor.fast_executemany = True

    def query(self, q, params=[], return_pd=False):
        if return_pd == False:
            return pd.read_sql_query(q, self.cnxn, params=params).to_dict('records')
        else:
            return pd.read_sql_query(q, self.cnxn, params=params)

    def insert(self, q, params=[], return_identity=False):
        if return_identity:
            # Need to have 'OUTPUT INSERTED.columnname' clause in query statement
            return self.cursor.execute(q, params).fetchone()[0]
        else:
            return self.cursor.execute(q, params)

    def batch_insert(self, q, params=[]):
        return self.cursor.executemany(q, params)

    def get_data_sp(self, sp, params=[]):
        if params == []:
            query = f'exec {sp}'
        elif params != []:
            params = ', '.join(['@'+param["name"]+"=" + "'" + str(param["value"]
                                                                  ).replace("'", "''") + "'" for param in params])
            query = f'exec {sp} {params}'

        return self.query(query)

    def insert_data_sp(self, sp, params=[]):
        if params == []:
            query = f'exec {sp}'
        elif params != []:
            params = ', '.join(
                ['@'+key+"=" + "'" + str(params[key]).replace("'", "''") + "'" for key in params])
            query = f'exec {sp} {params}'

        return self.cursor.execute(query)

    def delete(self, q, params=[]):
        return self.cursor.execute(q, params)


accessor = Accessor()
