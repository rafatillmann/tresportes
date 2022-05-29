from model.veiculo import Veiculo

class Motorista:
    def __init__(self, carga_horaria: str, veiculo: Veiculo):
        self.__id = None
        self.__carga_horaria = carga_horaria
        self.__veiculo = veiculo