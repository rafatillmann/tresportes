from dao.daoIncidente import DaoIncidente
from view.viewIncidente import ViewIncidente
from dao.daoRota import DaoRota

from model.incidente import Incidente

import datetime


class ControllerIncidente():

    def __init__(self, session):
        self.__dao_incidente = DaoIncidente
        self.__view = ViewIncidente()
        self.__dao_rota = DaoRota
        self.__session = session

    def options(self, route):
        while True:
            button, values = self.__view.options()
            if not self.__session.menu(button):
                if button == 'save':
                    if values['tipo'] == 'grave':
                        print('GRAVE')
                        route.fim = datetime.datetime.now()
                        self.__dao_rota.update(route)

                    incidente = Incidente(datetime.datetime.now() ,values['descricao'], route, values['tipo'])
                    self.__dao_incidente.insert(incidente)
                    break

    def read(self, id: int):
        return self.__dao_incidente.read(id)