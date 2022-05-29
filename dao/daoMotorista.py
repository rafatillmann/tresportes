from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.motorista import Motorista

class DaoMotorista(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'motorista'
        self.__records = []

        try:
            fields = 'id integer NOT NULL, nome varchar(255) NOT NULL, email varchar(255) NOT NULL, cpf integer NOT NULL, senha varchar(255) NOT NULL, carga_horaria integer NOT NULL, veiculo integer NOT NULL, PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY(veiculo) REFERENCES veiculo(id)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, motorista: Motorista):
        pass

    def update(self, motorista: Motorista):
        pass

    def delete(self, motorista: Motorista):
        pass

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record

    def list(self):
        return self.__records

    def populate(self):
        pass


DaoMotorista = DaoMotorista()