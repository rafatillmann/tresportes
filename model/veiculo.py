class Veiculo:
    def __init__(self, tipo: str, marca: str, modelo: str, placa: str, capacidade: int):
        self.__id = None
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__capacidade = capacidade

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca: str):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__marca

    @modelo.setter
    def modelo(self, modelo: str):
        self.__modelo = modelo

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa: str):
        self.__placa = placa

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: str):
        self.__capacidade = capacidade