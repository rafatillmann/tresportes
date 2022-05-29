from model.veiculo import Veiculo
from model.usuario import Usuario


class Motorista(Usuario):
    def __init__(self, nome: str, email: str, cpf: int, senha: str, carga_horaria: int, veiculo: Veiculo):
        super().__init__(nome, email, cpf, senha)
        self.__carga_horaria = carga_horaria
        self.__veiculo = veiculo

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria: int):
        self.__carga_horaria = carga_horaria

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo: Veiculo):
        self.__veiculo = veiculo
