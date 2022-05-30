from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.motorista import Motorista
from dao.daoVeiculo import DaoVeiculo


class DaoMotorista(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'motorista'
        self.__records = []
        self.__deleted = []
        self.__dao_veiculo = DaoVeiculo

        try:
            fields = 'id integer NOT NULL, nome varchar(255) NOT NULL, email varchar(255) NOT NULL, cpf integer NOT NULL, senha varchar(255) NOT NULL, carga_horaria integer NOT NULL, veiculo integer NOT NULL, deleted int DEFAULT 0, PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY(veiculo) REFERENCES veiculo(id)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, motorista: Motorista):
        fields = 'nome, email, cpf, senha, carga_horaria, veiculo'
        values = f'"{motorista.nome}", "{motorista.email}", "{motorista.cpf}", "{motorista.senha}", "{motorista.carga_horaria}", "{motorista.veiculo.id}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            motorista.id = self.__database.cursor.lastrowid
            self.__records.append(motorista)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, motorista: Motorista):
        fields = f'nome = "{motorista.nome}", email = "{motorista.email}", cpf = "{motorista.cpf}", senha = "{motorista.senha}", carga_horaria = "{motorista.carga_horaria}", veiculo = "{motorista.veiculo.id}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {motorista.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, motorista: Motorista):
        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET deleted=1 WHERE id = {motorista.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == motorista.id):
                    self.__records.remove(record)
                    self.__deleted.append(record)
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

    def deleted(self):
        return self.__deleted

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name} WHERE deleted=0').fetchall()

        for record in records:

            veiculo = self.__dao_veiculo.read(record[6])
            object = Motorista(record[1], record[2],
                               record[3], record[4], record[5], veiculo)
            object.id = record[0]
            self.__records.append(object)

        deleted = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name} WHERE deleted=1').fetchall()

        for delete in deleted:

            veiculo = self.__dao_veiculo.read(delete[6])
            object = Motorista(delete[1], delete[2],
                               delete[3], delete[4], delete[5], veiculo)
            object.id = delete[0]
            self.__deleted.append(object)


DaoMotorista = DaoMotorista()
