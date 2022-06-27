from controller.controllerCarga import ControllerCarga
from dao.daoPercuso import DaoPercurso
from dao.daoPonto import DaoPonto
from dao.daoRota import DaoRota
from model.google import API
from model.percurso import Percurso
from model.ponto import Ponto
from model.rota import Rota
from view.viewRota import ViewRota


class ControllerRota():

    def __init__(self, session):
        self.__view = ViewRota()
        self.__session = session
        self.__dao_rota = DaoRota
        self.__dao_ponto = DaoPonto
        self.__dao_percurso = DaoPercurso
        self.__api = API
        self.__controller_carga = ControllerCarga(session)

    def options(self):
        while True:
            list = self.__dao_rota.list()
            button, values = self.__view.options(list)
            if not self.__session.menu(button):
                if button == 'insert':
                    self.insert()
                elif 'edit' in button:
                    route = self.__dao_rota.read(int(button.split(':')[1]))
                    self.edit(route)
                elif 'view' in button:
                    route = self.__dao_rota.read(int(button.split(':')[1]))
                    self.view(route)
                elif button == 'finish':
                    self.finish()

    def insert(self):
        while True:
            try:
                button, values = self.__view.inicial()
                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'add':
                        route = self.add()
                        self.review(route)
                        break
            except Exception:
                self.__view.popUp()

    def review(self, route):
        while True:
            roads = self.__dao_percurso.read_route_not_finish(route)
            # loads = self.__controller_carga.read_by_route()
            button, values = self.__view.edit(route, roads)
            if not self.__session.menu(button):
                if button == 'cancel':
                    roads = self.__dao_percurso.read_route_not_finish(
                        route)
                    for road in roads:
                        self.__dao_percurso.delete(road)
                    self.__dao_rota.delete(route)
                    break
                elif button == 'edit':
                    self.add(route)
                elif button == 'save':
                    self.options()

    def edit(self, route):
        while True:
            roads = self.__dao_percurso.read_route_not_finish(route)
            # loads = self.__controller_carga.read_by_route()
            button, values = self.__view.edit(route, roads)
            if not self.__session.menu(button):
                if button == 'cancel':
                    break
                elif button == 'edit':
                    self.add(route)
                elif button == 'save':
                    self.options()

    def view(self, route):
        while True:
            roads = self.__dao_percurso.read_route_not_finish(route)
            # loads = self.__controller_carga.read_by_route()
            button, values = self.__view.view(route, roads)
            if not self.__session.menu(button):
                if button == 'back':
                    break

    def finish(self):
        while True:
            list = self.__dao_rota.deleted()
            button, values = self.__view.finish(list)
            if not self.__session.menu(button):
                if button == 'insert':
                    self.insert()
                elif button == 'finish':
                    self.finish()

    def add(self, route=None):
        while True:
            list = self.__controller_carga.read_unused()
            button, values = self.__view.select_load(
                ['R. Alipia Santana Martins', 'R. Delfino Conti'])
            if not self.__session.menu(button):
                if button == 'back':
                    break
                elif button == 'sel':
                    destinations = []
                    duration = []
                    origins = self.__dao_ponto.getOrigins()
                    if values['select']:
                        for value in values['select']:
                            destinations.append(
                                f'{value}, Florianópolis, Santa Catarina, Brasil')
                        matrix = self.__api.request(
                            origins.endereco, destinations)

                        for row in matrix.get('rows'):
                            for element in row.get('elements'):
                                duration.append(element.get(
                                    'duration').get('text'))

                        duration = self.convertTimes(duration)

                        dt = {}
                        for i, address in enumerate(matrix.get('destination_addresses')):
                            dt[address] = duration[i]

                        dt = {key: value for key, value in sorted(
                            dt.items(), key=lambda item: item[1])}

                        if route:
                            route.tempo_estimado = sum(dt.values())
                            self.__dao_rota.update(route)

                            roads = self.__dao_percurso.read_route_not_finish(
                                route)
                            for road in roads:
                                self.__dao_percurso.delete(road)
                        else:
                            route = Rota(tempo_estimado=sum(dt.values()))
                            self.__dao_rota.insert(route)

                        spots = []
                        spots.append(origins)
                        for key, value in dt.items():
                            spot = Ponto(endereco=key)
                            if self.__dao_ponto.insert(spot):
                                spots.append(spot)

                        for cur, nxt in zip(spots, spots[1:] + ['end']):
                            if nxt == 'end':
                                break
                            else:
                                road = Percurso(
                                    pontoA=cur, pontoB=nxt, rota=route)
                                self.__dao_percurso.insert(road)
                        return route
                    else:
                        break

    def convertTimes(self, array):

        duration = []
        for string in array:
            result = ''.join([i for i in string if i.isdigit() or i == ' '])

            if 'h' in string:
                values = result.split()
                minutes = int(values[0]) * 60 + int(values[1])
                duration.append(minutes)
            else:
                values = result.split()
                minutes = int(values[0])
                duration.append(minutes)

        return duration
