from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.incidente import Incidente


class DaoIncidente(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'incidente'
        self.__records = []

        try:
            fields = 'id integer NOT NULL, data varchar(255) NOT NULL, descricao varchar(255) NOT NULL, rota integer, tipo varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, incidente: Incidente):
        fields = 'data, descricao, rota, tipo'
        values = f'"{incidente.data}", "{incidente.descricao}", "{incidente.rota}", "{incidente.tipo}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            incidente.id = self.__database.cursor.lastrowid
            self.__records.append(incidente)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, incidente: Incidente):
        fields = f'data = "{incidente.data}", descricao = "{incidente.descricao}", rota = "{incidente.rota}", tipo = "{incidente.tipo}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {incidente.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, incidente: Incidente):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {incidente.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == incidente.id):
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
            object = Incidente(record[1], record[2], record[3], record[4])
            object.id = record[0]
            self.__records.append(object)


DaoIncidente = DaoIncidente()
