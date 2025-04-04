from abc import ABC

import mysql.connector
import pandas as pd
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


class Dbconfig(ABC):
    def __init__(self, host: str, user: str, password: str, dbname: str):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

    @staticmethod
    def connect(host: str, user: str, password: str, dbname: str) -> PooledMySQLConnection | MySQLConnectionAbstract:
        db_config = {
            "host": host,
            "user": user,
            "password": password,
            'database': dbname
        }

        conn = mysql.connector.connect(**db_config)
        return conn