from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.veiculo import Veiculo


class DaoVeiculo(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'veiculo'
        self.__records = []

        try:
            fields = 'id integer NOT NULL, tipo varchar(255) NOT NULL, marca varchar(255) NOT NULL, modelo varchar(255) NOT NULL, placa varchar(255) NOT NULL, capacidade integer NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, veiculo: Veiculo):
        fields = 'tipo, marca, modelo, placa, capacidade'
        values = f'"{veiculo.tipo}", "{veiculo.marca}", "{veiculo.modelo}", "{veiculo.placa}", "{veiculo.capacidade}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            veiculo.id = self.__database.cursor.lastrowid
            self.__records.append(veiculo)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, veiculo: Veiculo):
        fields = f'tipo = "{veiculo.tipo}", marca = "{veiculo.marca}", modelo = "{veiculo.modelo}", placa = "{veiculo.placa}", capacidade = "{veiculo.capacidade}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {veiculo.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, veiculo: Veiculo):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {veiculo.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == veiculo.id):
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

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:
            object = Veiculo(record[1], record[2],
                             record[3], record[4], record[5])
            object.id = record[0]
            self.__records.append(object)


DaoVeiculo = DaoVeiculo()
