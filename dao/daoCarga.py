from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from dao.daoCategoria import DaoCategoria
from dao.daoDestinatario import DaoDestinatario
from dao.daoRota import DaoRota
from database.db import DB
from model.carga import Carga
from model.rota import Rota


class DaoCarga(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'carga'
        self.__records = []
        self.__dao_destinatario = DaoDestinatario
        self.__dao_rota = DaoRota
        self.__dao_categoria = DaoCategoria

        try:
            fields = 'id integer NOT NULL, categoria integer, altura REAL NOT NULL, largura REAL NOT NULL, comprimento REAL NOT NULL, peso REAL NOT NULL, descricao varchar(255) NOT NULL, destinatario integer NOT NULL, rota integer, status varchar(255), PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, carga: Carga):
        fields = 'categoria, altura, largura, comprimento, peso, descricao, destinatario, rota, status'
        values = (carga.categoria.id, carga.altura, carga.largura, carga.comprimento,
                  carga.peso, carga.descricao, carga.destinatario.id, carga.rota.id if carga.rota else None, carga.status)
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', values)
            self.__database.connection.commit()

            carga.id = self.__database.cursor.lastrowid
            self.__records.append(carga)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, carga: Carga):
        fields = f'categoria = ?, altura = ?, largura = ?, comprimento = ?, peso = ?, descricao = ?, destinatario = ?, rota = ?, status = ?'
        values = (carga.categoria.id, carga.altura, carga.largura, carga.comprimento,
                  carga.peso, carga.descricao, carga.destinatario.id, carga.rota.id if carga.rota else None, carga.status)

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {carga.id}', values)
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, carga: Carga):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {carga.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == carga.id):
                    self.__records.remove(record)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record

    def read_unused(self):
        records = []
        for record in self.__records:
            if not record.rota:
                records.append(record)

        return records

    def read_by_route(self, route: Rota):
        result = []
        for record in self.__records:
            if record.rota == route:
                result.append(record)
        return result

    def list(self):
        return self.__records

    def populate(self):
        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:
            categoria = self.__dao_categoria.read(record[1])
            destinatario = self.__dao_destinatario.read(record[7])
            rota = self.__dao_rota.read(record[8])
            object = Carga(categoria, record[2], record[3], record[4],
                           record[5], record[6], destinatario, rota, record[9])
            object.id = record[0]
            self.__records.append(object)


DaoCarga = DaoCarga()
