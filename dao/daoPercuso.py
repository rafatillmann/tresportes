

from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from dao.daoPonto import DaoPonto
from dao.daoRota import DaoRota
from database.db import DB
from model.percurso import Percurso


class DaoPercurso(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'percurso'
        self.__records = []
        self.__dao_ponto = DaoPonto
        self.__dao_rota = DaoRota

        try:
            fields = 'id integer NOT NULL, inicio datetime, fim datetime, pontoA integer NOT NULL, pontoB integer NOT NULL, rota integer NOT NULL, PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY(pontoA) REFERENCES ponto(id), FOREIGN KEY(pontoB) REFERENCES ponto(id), FOREIGN KEY(rota) REFERENCES rota(id)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, percurso: Percurso):
        fields = 'inicio, fim, pontoA, pontoB, rota'
        values = (percurso.inicio, percurso.fim, percurso.pontoA.id,
                  percurso.pontoB.id, percurso.rota.id)
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES(?, ?, ?, ?, ?)', values)
            self.__database.connection.commit()

            percurso.id = self.__database.cursor.lastrowid
            self.__records.append(percurso)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, percurso: Percurso):
        fields = f'inicio = ?, fim = ?, pontoA = ?, pontoB = ?, rota= ?'
        values = (percurso.inicio, percurso.fim, percurso.pontoA.id,
                  percurso.pontoB.id, percurso.rota.id)

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {percurso.id}', values)
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, percurso: Percurso):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {percurso.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == percurso.id):
                    self.__records.remove(record)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record

    def read_route_not_finish(self, route):
        result = []
        for record in self.__records:
            if record.rota == route and not record.fim:
                result.append(record)
        return result

    def list(self):
        return self.__records

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:

            pontoA = self.__dao_ponto.read(record[3])
            pontoB = self.__dao_ponto.read(record[4])
            rota = self.__dao_rota.read(record[5])

            object = Percurso(record[1], record[2],
                              pontoA, pontoB, rota)
            object.id = record[0]
            self.__records.append(object)


DaoPercurso = DaoPercurso()
