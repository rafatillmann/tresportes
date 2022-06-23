from model.categoria import Categoria
from model.destinatario import Destinatario
from model.rota import Rota

class Carga():
    def __init__(self, categoria: Categoria, altura: float, largura: float, comprimento: float, peso: float, descricao: str, destinatario: Destinatario, rota: Rota, status: str):
        super().__init__(nome, email, cpf, senha)
        self.__categoria = categoria
        self.__altura = altura
        self.__largura = largura
        self.__comprimento = comprimento
        self.__peso = peso
        self.__descricao = descricao
        self.__destinatario = destinatario
        self.__rota = rota
        self.__status = 'Na transportadora'

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        self.__categoria = categoria

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura: float):
        self.__altura = altura
    
    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, largura: float):
        self.__largura = largura

    @property
    def comprimento(self):
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, comprimento: float):
        self.__comprimento = comprimento
    
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso: float):
        self.__peso = peso

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def destinatario(self):
        return self.__destinatario

    @destinatario.setter
    def destinatario(self, destinatario: Destinatario):
        self.__destinatario = destinatario

    @property
    def rota(self):
        return self.__rota

    @rota.setter
    def rota(self, rota: Rota):
        self.__rota = rota

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status
    