from model.usuario import Usuario


class Destinatario(Usuario):
    def __init__(self, nome: str = None, email: str = None, cpf: int = None, senha: str = None, cnpj: str = None, endereco: str = None, complemento: str = None, telefone: str = None):
        super().__init__(nome, email, cpf, senha)
        self.__cnpj = cnpj
        self.__endereco = endereco
        self.__complemento = complemento
        self.__telefone = telefone

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: int):
        self.__cnpj = cnpj

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento: str):
        self.__complemento = complemento

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
