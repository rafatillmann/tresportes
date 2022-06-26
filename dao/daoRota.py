from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from dao.daoMotorista import DaoMotorista
from database.db import DB
from model.motorista import Motorista
from model.rota import Rota


class DaoRota(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'rota'
        self.__records = []
        self.__deleted = []
        self.__dao_motorista = DaoMotorista

        try:
            fields = 'id integer NOT NULL, inicio datetime, fim datetime, tempo_estimado float, motorista integer, deleted int DEFAULT 0, PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY(motorista) REFERENCES motorista(id)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, rota: Rota):
        fields = 'inicio, fim, tempo_estimado, motorista'
        values = (rota.inicio, rota.fim, rota.tempo_estimado,
                  rota.motorista.id if rota.motorista else None)
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES(?, ?, ?, ?)', values)
            self.__database.connection.commit()

            rota.id = self.__database.cursor.lastrowid
            self.__records.append(rota)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, rota: Rota):
        fields = f'inicio = ?, fim = ?, tempo_estimado = ?, motorista = ?'
        values = (rota.inicio, rota.fim, rota.tempo_estimado,
                  rota.motorista.id if rota.motorista else None)

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {rota.id}', values)
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            print(error)
            self.__database.connection.rollback()
            return False

    def delete(self, rota: Rota):
        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET deleted=1 WHERE id = {rota.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == rota.id):
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

    def list(self):
        return self.__records

    def deleted(self):
        return self.__deleted

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name} WHERE deleted=0').fetchall()

        for record in records:

            motorista = self.__dao_motorista.read(record[4])
            object = Rota(record[1], record[2],
                          record[3], motorista)
            object.id = record[0]
            self.__records.append(object)

        deleted = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name} WHERE deleted=1').fetchall()

        for delete in deleted:

            motorista = self.__dao_motorista.read(record[4])
            object = Rota(record[1], record[2],
                          record[3], motorista)
            object.id = delete[0]
            self.__deleted.append(object)


DaoRota = DaoRota()
