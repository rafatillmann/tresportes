import hashlib
from random import randint
from model.destinatario import Destinatario
from dao.daoDestinatario import DaoDestinatario
from util.utils import cnpj_validate, cpf_validate, email_validate, generate_random_password
from view.viewCadastroDestinatario import ViewDestinatario


class ControllerDestinatario:

    def __init__(self, session):
        self.__dao_destinatario = DaoDestinatario
        self.__view = ViewDestinatario()
        self.__session = session

    def options(self):
        pass

    def insert(self):
        try:
            button, values = self.__view.display()
            if not self.__session.menu(button):
                if button == 'save':
                    cpf = cpf_validate(values['cpf/cnpj'])
                    cnpj = cnpj_validate(values['cpf/cnpj'])
                    if cpf or cnpj:
                        if email_validate(values['email']):
                            if self.read_by_email(values['email']):
                                self.__view.popUp(
                                    'Operação inválida, já existe um destinatário cadastrado com esse e-mail')
                            else:
                                password = values['senha'].encode()
                                password = hashlib.md5(
                                    password).hexdigest()
                                numbers = [
                                    char for char in values['cpf/cnpj'] if char.isdigit()]
                                doc = int(''.join(numbers))
                                destinatario = Destinatario(values['nome'], values['email'], doc if cpf else None, password,
                                                            doc if cnpj else None, values['endereco'], values['complemento'], values['telefone'])
                                self.__dao_destinatario.insert(destinatario)
                        else:
                            self.__view.popUp(
                                'Não foi possível finalizar o cadastro, e-mail inválido')
                    else:
                        self.__view.popUp(
                            'Não foi possível finalizar o cadastro, CPF/CNPJ inválido')
        except Exception as e:
            self.__view.popUp()

    def update(self, email: str = None):
        try:
            destinatario = self.__dao_destinatario.readByEmail(email)
            button, values = self.__view.display(destinatario)
            if not self.__session.menu(button):
                if button == 'save':
                    cpf = cpf_validate(values['cpf/cnpj'])
                    cnpj = cnpj_validate(values['cpf/cnpj'])
                    if cpf or cnpj:
                        if email_validate(values['email']):
                            password = values['senha'].encode()
                            password = hashlib.md5(
                                password).hexdigest()

                            numbers = [
                                char for char in values['cpf/cnpj'] if char.isdigit()]
                            doc = int(''.join(numbers))

                            destinatario.nome = values['nome']
                            destinatario.email = values['email']
                            destinatario.cpf = doc if cpf else None
                            destinatario.senha = password
                            destinatario.cnpj = doc if cnpj else None
                            destinatario.endereco = values['endereco']
                            destinatario.complemento = values['complemento']
                            destinatario.telefone = values['telefone']

                            self.__dao_destinatario.update(destinatario)

                        else:
                            self.__view.popUp(
                                'Não foi possível finalizar o cadastro, e-mail inválido')
                    else:
                        self.__view.popUp(
                            'Não foi possível finalizar o cadastro, CPF/CNPJ inválido')
        except Exception:
            self.__view.popUp()

    def delete(self):
        pass

    def read(self, id: int):
        return self.__dao_destinatario.read(id)

    def read_by_email(self, email):
        return self.__dao_destinatario.readByEmail(email)
