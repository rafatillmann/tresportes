from view.viewGerente import ViewGerente
from dao.daoGerente import DaoGerente
from model.gerente import Gerente


class ControllerGerente:

    def __init__(self):
        self.__dao_ = DaoGerente
        self.__view = ViewGerente()

    def options(self):
        pass

    def insert(self):
        pass

    def update(self, gerente: Gerente):
        pass

    def delete(self):
        pass

    def read(self, id: int):
        return self.__dao_gerente.read(id)
