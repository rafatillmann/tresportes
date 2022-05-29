from view.viewMotorista import ViewMotorista
from dao.daoMotorista import DaoMotorista
from dao.daoVeiculo import DaoVeiculo


class ControllerMotorista:

    def __init__(self):
        self.__dao_motorista = DaoMotorista
        self.__dao_veiculo = DaoVeiculo
        self.__view = ViewMotorista()

    def options(self):
        list = self.__dao_motorista.list()
        option = self.__view.options(list)

        if option == 'insert':
            self.insert()

    def insert(self):
        try:
            value = self.__view.insert()
        except Exception:
            pass

    def update(self):
        try:
            value = self.__view.update()
        except Exception:
            pass

    def delete(self):
        pass

    def read(self):
        pass
