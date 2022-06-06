from random import randint
from tkinter import N
from view.viewMotorista import ViewMotorista
from dao.daoMotorista import DaoMotorista
from dao.daoVeiculo import DaoVeiculo
from model.motorista import Motorista
from model.veiculo import Veiculo


class ControllerMotorista:

    def __init__(self):
        self.__dao_motorista = DaoMotorista
        self.__dao_veiculo = DaoVeiculo
        self.__view = ViewMotorista()

    def options(self):
        while True:
            list = self.__dao_motorista.list()
            button, values = self.__view.options(list)

            if button == None:
                exit()
            elif button == 'insert':
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

                if button == None:
                    exit()
                elif button == 'cancel':
                    break
                elif button == 'save':
                    veiculo = Veiculo(values['tipo'], values['marca'], values['modelo'],
                                      values['placa'], int(values['capacidade']), int(values['largura']), int(values['comprimento']), int(values['altura']))
                    motorista = Motorista(values['nome'], values['email'],
                                          int(values['cpf']), randint(300, 600), int(values['carga_horaria']), veiculo)

                    if self.__dao_veiculo.insert(veiculo) and self.__dao_motorista.insert(motorista):
                        # self.__view.popUp(
                        #     f'Login tempotário do motorista. E-mail: {motorista.email} Senha: {motorista.senha}')
                        break
                    else:
                        self.__view.popUp()
            except Exception:
                self.__view.popUp()

    def update(self, motorista: Motorista):
        try:
            button, values = self.__view.display(motorista)

            if button == None:
                exit()
            elif button == 'cancel':
                pass
            elif button == 'delete':
                self.delete(motorista)
            elif button == 'save':
                veiculo = motorista.veiculo
                veiculo.tipo = values['tipo']
                veiculo.timarcapo = values['marca']
                veiculo.modelo = values['modelo']
                veiculo.placa = values['placa']
                veiculo.capacidade = int(values['capacidade'])
                veiculo.largura = int(values['largura'])
                veiculo.comprimento = int(values['comprimento'])
                veiculo.altura = int(values['altura'])

                motorista.nome = values['nome']
                motorista.email = values['email']
                motorista.cpf = values['cpf']
                motorista.carga_horaria = int(values['carga_horaria'])
                motorista.veiculo = veiculo

                self.__dao_veiculo.update(veiculo)
                self.__dao_motorista.update(motorista)
        except Exception:
            self.__view.popUp()

    def delete(self, motorista: Motorista):
        self.__dao_veiculo.delete(motorista.veiculo)
        self.__dao_motorista.delete(motorista)

    def read(self, id: int):
        return self.__dao_motorista.read(id)

    def del_driver(self):
        try:
            list = self.__dao_motorista.deleted()
            button, values = self.__view.del_driver(list)

            if button == None:
                exit()
            elif button == 'insert':
                self.insert()
            elif button == 'back':
                self.options()
            elif button == 'del_driver':
                self.del_driver()

        except Exception:
            self.__view.popUp()
