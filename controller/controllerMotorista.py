from view.viewMotorista import ViewMotorista
from dao.daoMotorista import DaoMotorista
from dao.daoVeiculo import DaoVeiculo


class ControllerMotorista:

    def __init__(self):
        self.__dao_motorista = DaoMotorista
        self.__dao_veiculo = DaoVeiculo
        self.__view = ViewMotorista()

    def options(self):
        option = self.__view.options()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def read(self):
        pass
