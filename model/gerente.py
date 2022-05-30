from model.usuario import Usuario


class Gerente(Usuario):
    def __init__(self, nome: str, email: str, cpf: int, senha: str):
        super().__init__(nome, email, cpf, senha)
