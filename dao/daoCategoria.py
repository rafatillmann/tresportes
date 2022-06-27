from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.categoria import Categoria


class DaoCategoria(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'categoria'
        self.__records = []

        try:
            fields = 'id integer NOT NULL, nome varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, categoria: Categoria):
        fields = 'nome'
        values = f'"{categoria.nome}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            categoria.id = self.__database.cursor.lastrowid
            self.__records.append(categoria)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, categoria: Categoria):
        fields = f'nome = "{categoria.nome}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {categoria.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, categoria: Categoria):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {categoria.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == categoria.id):
                    self.__records.remove(record)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record

    def read_by_name(self, nome: str):
        for record in self.__records:
            if record.nome == nome:
                return record

    def list(self):
        return self.__records

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:
            object = Categoria(record[1])
            object.id = record[0]
            self.__records.append(object)


DaoCategoria = DaoCategoria()
