import sqlite3

class Database():
    def __init__(self):
        self.__connection = sqlite3.connect('./database/database.db')
        self.__cursor = self.__connection.cursor()

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor

DB = Database()