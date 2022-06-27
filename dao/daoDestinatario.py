from sqlite3 import OperationalError
from dao.abstractDao import AbstractDao
from database.db import DB
from model.destinatario import Destinatario


class DaoDestinatario(AbstractDao):
    def __init__(self):
        self.__database = DB
        self.__table_name = 'destinatario'
        self.__records = []

        try:
            fields = 'id integer NOT NULL, nome varchar(255) NOT NULL, email varchar(255) NOT NULL, cpf integer NOT NULL, senha varchar(255), cnpj integer NOT NULL, endereco varchar(255) NOT NULL, complemento varchar(255), telefone varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, destinatario: Destinatario):
        fields = 'nome, email, cpf, senha, cnpj, endereco, complemento, telefone'
        values = f'"{destinatario.nome}", "{destinatario.email}", "{destinatario.cpf}", "{destinatario.senha}", "{destinatario.cnpj}", "{destinatario.endereco}", "{destinatario.complemento}", "{destinatario.telefone}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            destinatario.id = self.__database.cursor.lastrowid
            self.__records.append(destinatario)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, destinatario: Destinatario):
        fields = f'nome = "{destinatario.nome}", email = "{destinatario.email}", cpf = "{destinatario.cpf}", senha = "{destinatario.senha}", cnpj= "{destinatario.cnpj}", endereco = "{destinatario.endereco}", complemento = "{destinatario.complemento}", telefone = "{destinatario.telefone}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {destinatario.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, destinatario: Destinatario):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {destinatario.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == destinatario.id):
                    self.__records.remove(record)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record

    def readByCPF(self, cpf):
        for record in self.__records:
            if record.cpf == cpf:
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

            object = Destinatario(record[1], record[2],
                                  record[3], record[4], record[5], record[6], record[7], record[8])
            object.id = record[0]
            self.__records.append(object)


DaoDestinatario = DaoDestinatario()
