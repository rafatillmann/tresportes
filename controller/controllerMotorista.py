from random import randint
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
        list = self.__dao_motorista.list()
        button, values = self.__view.options(list)

        if button == 'insert':
            self.insert()
        elif button == 'edit':
            if len(values['select']) > 0:
                motorista = self.read(values['select'][0].id)
                self.update(motorista)
        elif button == 'search':
            self.search()

    def insert(self):
        try:
            button, values = self.__view.display()

            if button == 'cancel':
                pass
            elif button == 'save':
                veiculo = Veiculo(values['tipo'], values['marca'], values['modelo'],
                                  values['placa'], int(values['capacidade']), int(values['largura']), int(values['comprimento']), int(values['altura']))
                motorista = Motorista(values['nome'], values['email'],
                                      values['cpf'], randint(300, 600), int(values['carga_horaria']), veiculo)

                self.__dao_veiculo.insert(veiculo)
                self.__dao_motorista.insert(motorista)
        except Exception:
            pass

    def update(self, motorista: Motorista):
        try:
            button, values = self.__view.display(motorista)

            if button == 'cancel':
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
            pass

    def delete(self, motorista: Motorista):
        self.__dao_veiculo.delete(motorista.veiculo)
        self.__dao_motorista.delete(motorista)

    def read(self, id: int):
        return self.__dao_motorista.read(id)
