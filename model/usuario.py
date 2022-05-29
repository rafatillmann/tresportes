class Usuario:
    def __init__(self, nome: str, email: str, cpf: int, senha: str):
        self.__id = None
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__senha = senha