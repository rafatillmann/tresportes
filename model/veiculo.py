class Veiculo:
    def __init__(self, tipo: str, marca: str, modelo: str, placa: str, capacidade: int):
        self.__id = None
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__capacidade = capacidade