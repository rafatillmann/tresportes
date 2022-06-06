from random import randint
from model.destinatario import Destinatario
from dao.daoDestinatario import DaoDestinatario
from view.viewCadastroDestinatario import ViewDestinatario


class ControllerDestinatario:

    def __init__(self):
        self.__dao_destinatario = DaoDestinatario
        self.__view = ViewDestinatario()

    def options(self):
        pass

    def insert(self):
        try:
            button, values = self.__view.display()

            if button == 'save':
                destinatario = Destinatario(values['nome'], values['email'], values['cpf'], values['senha'],
                                            values['cpf'], values['endereco'], values['complemento'], values['telefone'])

                self.__dao_destinatario.insert(destinatario)

        except Exception:
            self.__view.popUp()

    def update(self, email: str = None):
        try:
            destinatario = self.__dao_destinatario.readByEmail(email)
            button, values = self.__view.display(destinatario)

            if button == 'save':
                destinatario.nome = values['nome']
                destinatario.email = values['email']
                destinatario.cpf = values['cpf']
                destinatario.senha = values['senha']
                destinatario.cnpj = values['cpf']
                destinatario.endereco = values['endereco']
                destinatario.complemento = values['complemento']
                destinatario.telefone = values['telefone']

                self.__dao_destinatario.update(destinatario)
        except Exception:
            self.__view.popUp()

    def delete(self):
        pass

    def read(self, id: int):
        return self.__dao_destinatario.read(id)
