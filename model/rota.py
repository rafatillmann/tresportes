from datetime import datetime
from model.motorista import Motorista


class Rota:
    def __init__(self, inicio: datetime, fim: datetime, tempo_estimado: float, motorista: Motorista):
        self.__id = None
        self.__inicio = inicio
        self.__fim = fim
        self.__tempo_estimado = tempo_estimado
        self.__motorista = motorista

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
    def motorista(self):
        return self.__motorista

    @motorista.setter
    def motorista(self, motorista: Motorista):
        self.__motorista = motorista

    @property
    def tempo_estimado(self):
        return self.__tempo_estimado

    @tempo_estimado.setter
    def tempo_estimado(self, tempo_estimado: float):
        self.__tempo_estimado = tempo_estimado
