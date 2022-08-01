from dao.daoIncidente import DaoIncidente
from view.viewIncidente import ViewIncidente

from model.incidente import Incidente

import datetime


class ControllerIncidente():

    def __init__(self, session):
        self.__dao_incidente = DaoIncidente
        self.__view = ViewIncidente()
        self.__session = session

    def options(self, route):
        while True:
            button, values = self.__view.options()
            if not self.__session.menu(button):
                if button == 'save':
                    print(values)
                    incidente = Incidente(datetime.datetime.now() ,values['descricao'], route, values['tipo'])
                    self.__dao_incidente.insert()
                    break

    def read(self, id: int):
        return self.__dao_incidente.read(id)