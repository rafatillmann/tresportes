from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.ponto import Ponto


class DaoPonto(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'ponto'
        self.__records = []

        try:
            fields = 'id integer NOT NULL, descricao varchar(255), endereco varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, ponto: Ponto):
        fields = 'descricao, endereco'
        values = (ponto.descricao, ponto.endereco)
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES(?, ?)', values)
            self.__database.connection.commit()

            ponto.id = self.__database.cursor.lastrowid
            self.__records.append(ponto)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, ponto: Ponto):
        fields = f'descricao = ?, endereco = ?'
        values = (ponto.descricao, ponto.endereco)

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {ponto.id}', values)
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, ponto: Ponto):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {ponto.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == ponto.id):
                    self.__records.remove(record)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record

    def list(self):
        return self.__records

    def getOrigins(self):
        for record in self.__records:
            if(record.endereco == 'R. Lauro Linhares - Trindade, Florianópolis - SC, Brazil'):
                return record

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:
            object = Ponto(record[1], record[2])
            object.id = record[0]
            self.__records.append(object)


DaoPonto = DaoPonto()
