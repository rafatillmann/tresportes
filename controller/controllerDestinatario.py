import hashlib
from dao.daoDestinatario import DaoDestinatario
from util.session import Session
from util.utils import cnpj_validate, cpf_validate, email_validate
from view.viewCadastroDestinatario import ViewDestinatario
from model.destinatario import Destinatario


class ControllerDestinatario:

    def __init__(self, session):
        self.__dao_destinatario = DaoDestinatario
        self.__view = ViewDestinatario()        
        self.__session = session

    def options(self):
        # while True:
        #     list = self.__dao_destinatario.list()
        #     button, values = self.__view.options(list)
        #     if not self.__session.menu(button):
        #         if button == 'insert':
        #             self.insert()
        #         elif button == 'edit':
        #             if len(values['select']) > 0:
        #                 destinatario = self.read(values['select'][0].id)
        #                 self.update(destinatario)
        pass

    def insert(self):
        while True:
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
                                    if self.__dao_destinatario.insert(
                                            destinatario):
                                        break
                                    else:
                                        self.__view.popUp()
                            else:
                                self.__view.popUp(
                                    'Não foi possível finalizar o cadastro, e-mail inválido')
                        else:
                            self.__view.popUp(
                                'Não foi possível finalizar o cadastro, CPF/CNPJ inválido')
            except Exception as e:
                self.__view.popUp(e)

    def update(self):
        
        try:
            destinatario = Session.user
            button, values = self.__view.display(destinatario)
            if not self.__session.menu(button):
                if button == 'delete':
                    self.delete(destinatario)
                    #mandar de volta para o menu                    

                elif button == 'save':
                    cpf = cpf_validate(values['cpf/cnpj'])
                    cnpj = cnpj_validate(values['cpf/cnpj'])
                    if cpf or cnpj:
                        if email_validate(values['email']):
                            if values['senha']:
                                password = values['senha'].encode()
                                password = hashlib.md5(
                                    password).hexdigest()
                            else:
                                password = destinatario.senha

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
                                'Não foi possível finalizar o cadastro: e-mail inválido')
                    else:
                        self.__view.popUp(
                            'Não foi possível finalizar o cadastro: CPF/CNPJ inválido')

        except Exception:
            self.__view.popUp()

    def delete(self, destinatario: Destinatario):
        if self.__dao_destinatario.delete(destinatario):
            self.__view.popUp(
                'Seu cadastro foi removido com sucesso')
            return True
        else:
            return False

    def read(self, id: int):
        return self.__dao_destinatario.read(id)

    def read_by_email(self, email):
        return self.__dao_destinatario.readByEmail(email)
