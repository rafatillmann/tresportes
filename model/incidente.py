import datetime
from model.rota import Rota

class Incidente():

    def __init__(self, data: str, descricao: str, rota: Rota, tipo: str):
        self.__id = None
        self.__data = data
        self.__descricao = descricao
        self.__rota = rota
        self.__tipo = tipo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def rota(self):
        return self.__rota

    @rota.setter
    def rota(self, rota: str):
        self.__rota = rota

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo
