import hashlib
from util.utils import cpf_validate, email_validate, generate_random_password
from view.viewCadastroMotorista import ViewCadastroMotorista
from dao.daoMotorista import DaoMotorista
from dao.daoVeiculo import DaoVeiculo
from model.motorista import Motorista
from model.veiculo import Veiculo


class ControllerMotorista():

    def __init__(self, session):
        self.__dao_motorista = DaoMotorista
        self.__dao_veiculo = DaoVeiculo
        self.__view = ViewCadastroMotorista()
        self.__session = session

    def options(self):
        while True:
            list = self.__dao_motorista.list()
            button, values = self.__view.options(list)
            if not self.__session.menu(button):
                if button == 'insert':
                    self.insert()
                elif button == 'edit':
                    if len(values['select']) > 0:
                        motorista = self.read(values['select'][0].id)
                        self.update(motorista)
                elif button == 'del_driver':
                    self.del_driver()

    def insert(self):
        while True:
            try:
                button, values = self.__view.display()

                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'save':
                        if cpf_validate(values['cpf']):
                            if email_validate(values['email']):
                                if self.read_by_email(values['email']):
                                    self.__view.popUp(
                                        'Operação inválida, já existe um motorista cadastrado com esse e-mail')
                                else:
                                    passwd = generate_random_password()
                                    password = passwd.encode()
                                    password = hashlib.md5(
                                        password).hexdigest()
                                    numbers = [
                                        char for char in values['cpf'] if char.isdigit()]
                                    doc = int(''.join(numbers))
                                    veiculo = Veiculo(values['tipo'], values['marca'], values['modelo'],
                                                      values['placa'], int(values['capacidade']), int(values['largura']), int(values['comprimento']), int(values['altura']))
                                    motorista = Motorista(values['nome'], values['email'],
                                                          doc, password, int(values['carga_horaria']), veiculo)

                                    if self.__dao_veiculo.insert(veiculo) and self.__dao_motorista.insert(motorista):
                                        self.__view.popUp(
                                            f'Login tempotário do motorista, repasse essas informações.\nE-mail: {motorista.email}\nSenha: {passwd}')
                                        break
                                    else:
                                        self.__view.popUp()
                            else:
                                self.__view.popUp(
                                    'Não foi possível finalizar o cadastro, e-mail inválido')
                        else:
                            self.__view.popUp(
                                'Não foi possível finalizar o cadastro, CPF inválido')
            except Exception as e:
                self.__view.popUp(e)

    def update(self, motorista: Motorista):
        while True:
            try:
                button, values = self.__view.display(motorista)

                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'delete':
                        if self.delete(motorista):
                            break
                        else:
                            self.__view.popUp()
                    elif button == 'save':
                        if cpf_validate(values['cpf']):
                            if email_validate(values['email']):
                                veiculo = motorista.veiculo
                                veiculo.tipo = values['tipo']
                                veiculo.marca = values['marca']
                                veiculo.modelo = values['modelo']
                                veiculo.placa = values['placa']
                                veiculo.capacidade = int(values['capacidade'])
                                veiculo.largura = int(values['largura'])
                                veiculo.comprimento = int(
                                    values['comprimento'])
                                veiculo.altura = int(values['altura'])

                                numbers = [
                                    char for char in values['cpf'] if char.isdigit()]
                                doc = int(''.join(numbers))

                                motorista.nome = values['nome']
                                motorista.email = values['email']
                                motorista.cpf = doc
                                motorista.carga_horaria = int(
                                    values['carga_horaria'])
                                motorista.veiculo = veiculo

                                if self.__dao_veiculo.update(veiculo) and self.__dao_motorista.update(motorista):
                                    break
                                else:
                                    self.__view.popUp()
                            else:
                                self.__view.popUp(
                                    'Não foi possível finalizar o cadastro, e-mail inválido')
                        else:
                            self.__view.popUp(
                                'Não foi possível finalizar o cadastro, CPF inválido')
            except Exception:
                self.__view.popUp()

    def delete(self, motorista: Motorista):
        if self.__dao_veiculo.delete(motorista.veiculo) and self.__dao_motorista.delete(motorista):
            return True
        else:
            return False

    def read(self, id: int):
        return self.__dao_motorista.read(id)

    def read_by_email(self, email):
        return self.__dao_motorista.readByEmail(email)

    def del_driver(self):
        try:
            list = self.__dao_motorista.deleted()
            button, values = self.__view.del_driver(list)

            if not self.__session.menu(button):
                if button == 'insert':
                    self.insert()
                elif button == 'back':
                    self.options()
                elif button == 'del_driver':
                    self.del_driver()

        except Exception:
            self.__view.popUp()
