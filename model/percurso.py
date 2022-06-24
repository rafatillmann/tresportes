from datetime import datetime

from model.ponto import Ponto
from model.rota import Rota


class Percurso:
    def __init__(self, inicio: datetime = None, fim: datetime = None, pontoA: Ponto = None, pontoB: Ponto = None, rota: Rota = None):
        self.__id = None
        self.__inicio = inicio
        self.__fim = fim
        self.__pontoA = pontoA
        self.__pontoB = pontoB
        self.__rota = rota

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio: datetime):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim: datetime):
        self.__fim = fim

    @property
    def pontoA(self):
        return self.__pontoA

    @pontoA.setter
    def pontoA(self, pontoA: Ponto):
        self.__pontoA = pontoA

    @property
    def pontoB(self):
        return self.__pontoB

    @pontoB.setter
    def pontoB(self, pontoB: Ponto):
        self.__pontoB = pontoB

    @property
    def rota(self):
        return self.__rota

    @rota.setter
    def rota(self, rota: Rota):
        self.__rota = rota
