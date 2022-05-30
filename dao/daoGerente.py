from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.gerente import Gerente


class DaoGerente(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'gerente'
        self.__records = []

        try:
            fields = 'id integer NOT NULL, nome varchar(255) NOT NULL, email varchar(255) NOT NULL, cpf integer NOT NULL, senha varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, gerente: Gerente):
        fields = 'nome, email, cpf, senha'
        values = f'"{gerente.nome}", "{gerente.email}", "{gerente.cpf}", "{gerente.senha}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            gerente.id = self.__database.cursor.lastrowid
            self.__records.append(gerente)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, gerente: Gerente):
        fields = f'nome = "{gerente.nome}", email = "{gerente.email}", cpf = "{gerente.cpf}", senha = "{gerente.senha}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {gerente.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, gerente: Gerente):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {gerente.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == gerente.id):
                    self.__records.remove(record)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record

    def readByEmail(self, email: str):
        for record in self.__records:
            if(record.email == email):
                return record

    def list(self):
        return self.__records

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:

            object = Gerente(record[1], record[2],
                               record[3], record[4])
            object.id = record[0]
            self.__records.append(object)


DaoGerente = DaoGerente()
