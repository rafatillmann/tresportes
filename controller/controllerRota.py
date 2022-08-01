from datetime import datetime
from controller.controllerCarga import ControllerCarga
from dao.daoPercuso import DaoPercurso
from dao.daoPonto import DaoPonto
from dao.daoRota import DaoRota
from dao.daoMotorista import DaoMotorista
from model.google import API
from model.percurso import Percurso
from model.ponto import Ponto
from model.rota import Rota
from util.session import Session
from view.viewRota import ViewRota
from view.viewMotorista import ViewMotorista
from view.viewIncidente import ViewIncidente


class ControllerRota():

    def __init__(self, session):
        self.__view = ViewRota()
        self.__session = session
        self.__dao_rota = DaoRota
        self.__dao_ponto = DaoPonto
        self.__dao_percurso = DaoPercurso
        self.__api = API
        self.__controller_carga = ControllerCarga(session)
        self.__view_motorista = ViewMotorista()
        self.__view_incident = ViewIncidente()
        self.__dao_motorista = DaoMotorista

    def options(self):
        while True:
            if Session.type == 'Motorista':
                list = self.__dao_rota.list_by_motorista(Session.user)
                button, values = self.__view_motorista.options(list)
                if not self.__session.menu(button):
                    if 'view' in button:
                        route = self.__dao_rota.read(int(button.split(':')[1]))
                        self.view(route)
                    elif button == 'finish':
                        self.finish()
            elif Session.type == 'Gerente':
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
                        if route:
                            self.review(route)
                            break
                        else:
                            pass
            except Exception:
                self.__view.popUp()

    def review(self, route):
        while True:
            roads = self.__dao_percurso.read_route_not_finish(route)
            loads = self.__controller_carga.read_by_route(route)
            button, values = self.__view.edit(route, roads, loads)
            if not self.__session.menu(button):
                if button == 'cancel':
                    roads = self.__dao_percurso.read_route(
                        route)
                    for road in roads:
                        self.__dao_percurso.delete(road)
                        if road.pontoA != self.__dao_ponto.getOrigins():
                            self.__dao_ponto.delete(road.pontoA)
                        self.__dao_ponto.delete(road.pontoB)

                    for load in loads:
                        load.rota = None
                        self.__controller_carga.update_data(load)

                    self.__dao_rota.delete(route)
                    break
                elif button == 'edit':
                    self.add(route, loads)
                elif button == 'allocation':
                    pass
                elif button == 'save':
                    self.options()

    def edit(self, route):
        try:
            while True:
                roads = self.__dao_percurso.read_route_not_finish(route)
                loads = self.__controller_carga.read_by_route(route)
                button, values = self.__view.edit(route, roads, loads)
                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'edit':
                        self.add(route, loads)
                    elif button == 'allocation':
                        self.allocDriver(route)
                    elif button == 'save':
                        self.options()
        except Exception as e:
            print(e)

    def view(self, route: Rota):
        try:
            while True:
                if Session.type == 'Gerente':
                    roads = self.__dao_percurso.read_route_not_finish(route)
                    loads = self.__controller_carga.read_by_route(route)
                    button, values = self.__view.view(route, roads, loads)
                    if not self.__session.menu(button):
                        if button == 'back':
                            break
                elif Session.type == 'Motorista':
                    roads = self.__dao_percurso.read_route_not_finish(route)
                    loads = self.__controller_carga.read_by_route(route)
                    button, values = self.__view_motorista.view(
                        route, roads, loads)
                    if not self.__session.menu(button):
                        if button == 'back':
                            break
                        elif 'start' in button:
                            road = self.__dao_percurso.read(
                                int(button.split(':')[1]))
                            if not road.inicio:
                                road.inicio = datetime.now()
                                self.__dao_percurso.update(road)
                                origin = self.__dao_ponto.getOrigins()
                                loads = self.__controller_carga.read_by_route(
                                    route)
                                for load in loads:
                                    if load.destinatario.endereco == road.pontoB.endereco:
                                        load.status = 'Saiu para entrega'
                                        self.__controller_carga.update_data(
                                            load)
                                if origin.descricao == road.pontoA.descricao:
                                    route.inicio = datetime.now()
                                    self.__dao_rota.update(route)
                        elif 'finish' in button:
                            road = self.__dao_percurso.read(
                                int(button.split(':')[1]))
                            if not road.fim and road.inicio:
                                road.fim = datetime.now()
                                self.__dao_percurso.update(road)
                                loads = self.__controller_carga.read_by_route(
                                    route)
                                for load in loads:
                                    if load.destinatario.endereco == road.pontoB.endereco:
                                        load.status = 'Entregue'
                                        self.__controller_carga.update_data(
                                            load)
                                if len(roads) == 1:
                                    route.fim = datetime.now()
                                    self.__dao_rota.update(route)
                            else:
                                pass
                        elif 'incident' in button:
                            self.__view_incident.options(route)
        except Exception as e:
            print(e)

    def finish(self):
        while True:
            if Session.type == 'Gerente':
                list = self.__dao_rota.finish()
                button, values = self.__view.finish(list)
                if not self.__session.menu(button):
                    if button == 'insert':
                        self.insert()
                    elif button == 'finish':
                        self.finish()
                    elif 'view' in button:
                        route = self.__dao_rota.read(int(button.split(':')[1]))
                        self.view(route)
            elif Session.type == 'Motorista':
                list = self.__dao_rota.finish_by_motorista(Session.user)
                button, values = self.__view_motorista.finish(list)
                if not self.__session.menu(button):
                    if button == 'finish':
                        self.finish()
                    elif 'view' in button:
                        route = self.__dao_rota.read(int(button.split(':')[1]))
                        self.view(route)

    def add(self, route=None, loads=None):
        try:
            while True:
                list = self.__controller_carga.read_unused()
                if loads:
                    for load in loads:
                        list.append(load)
                button, values = self.__view.select_load(list)
                if not self.__session.menu(button):
                    if button == 'back':
                        break
                    elif button == 'sel':
                        destinations = []
                        origins = self.__dao_ponto.getOrigins()
                        if values['select']:
                            for value in values['select']:
                                destinations.append(
                                    f'{value.destinatario.endereco}, Florianópolis, Santa Catarina, Brasil')

                            try:
                                matrix = self.__api.request(
                                    origins.endereco, destinations)
                            except Exception:
                                self.__view.popUp(
                                    'Não foi possível definir o percurso da rota, tente novamente!')
                                break

                            dt, addresses = self.createRoute(matrix, values)

                            if route:
                                route.tempo_estimado = sum(dt.values())
                                self.__dao_rota.update(route)

                                roads = self.__dao_percurso.read_route(
                                    route)
                                for road in roads:
                                    self.__dao_percurso.delete(road)
                            else:
                                route = Rota(tempo_estimado=sum(dt.values()))
                                self.__dao_rota.insert(route)

                            if loads:
                                for load in loads:
                                    load.rota = None
                                    self.__controller_carga.update_data(load)

                            for value in values['select']:
                                value.rota = route
                                self.__controller_carga.update_data(value)

                            spots = []
                            spots.append(origins)
                            for key, value in dt.items():
                                spot = Ponto(
                                    descricao=key, endereco=addresses[key])
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
        except Exception:
            self.__view.popUp()

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

    def createRoute(self, matrix, values):
        duration = []
        for row in matrix.get('rows'):
            for element in row.get('elements'):
                duration.append(element.get('duration').get('text'))

        duration = self.convertTimes(duration)
        dt = {}
        addresses = {}
        for i, address in enumerate(matrix.get('destination_addresses')):
            dt[address] = duration[i]
            addresses[address] = values['select'][i].destinatario.endereco

        dt = {key: value for key, value in sorted(
            dt.items(), key=lambda item: item[1])}

        return dt, addresses

    def allocDriver(self, route: Rota):
        while True:
            list = self.__dao_motorista.list()
            button, values = self.__view.allocDriver(list)
            rotas = self.__dao_rota.list()
            if not self.__session.menu(button):
                if button == 'sel':
                    if len(values['select']) > 0:
                        motorista = values['select'][0]
                        for mot in rotas:
                            if mot.motorista.id == motorista.id: #verifica se ele já não está alocado em outra rota                            
                                self.__view.popUp('Motorista já alocado: selecione outro motorista')
                                break                                
                            elif motorista.carga_horaria < route.tempo_estimado:
                                self.__view.popUp('Carga horária do motorista excedida: selecione outro motorista')
                                break
                            else:
                                route.motorista = motorista
                                self.__dao_rota.update(route)
                                break
                elif button == 'back':
                    break
