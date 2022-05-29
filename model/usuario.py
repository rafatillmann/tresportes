class Usuario:
    def __init__(self, nome: str, email: str, cpf: int, senha: str):
        self.__id = None
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__senha = senha

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha