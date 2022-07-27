from dao.daoIncidente import DaoIncidente
from view.viewIncidente import ViewIncidente

from model.incidente import Incidente


class ControllerIncidente():

    def __init__(self, session):
        self.__dao_incidente = DaoIncidente
        self.__view = ViewIncidente()
        self.__session = session

    def options(self):
        while True:
            list = self.__dao_incidente.list()
            button, values = self.__view.options(list)
            if not self.__session.menu(button):
                if button == 'insert':
                    self.insert()
                elif 'edit' in button:
                    incidente = self.__dao_incidente.read(int(button.split(':')[1]))
                    self.update(incidente)

    def insert(self):
        while True:
            try:
                button, values = self.__view.inicial()
                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'save':
                        break
            except Exception:
                self.__view.popUp()

    def update(self, incidente: Incidente):
        while True:
            try:
                button, values = self.__view.edit(incidente)
                if not self.__session.menu(button):
                    if button == 'delete':
                        self.__dao_incidente.delete(incidente)
                        break
                    elif button == 'save':
                        incidente.categoria = self.__dao_categoria.read_by_name(values['categoria'])
                        incidente.descricao = float(values['altura'])
                        incidente.descricao = float(values['largura'])
                        incidente.descricao = float(values['comprimento'])
                        incidente.descricao = float(values['peso'])
                        incidente.descricao = values['descricao']
                        incidente.destinatario = self.__dao_destinatario.readByCPF(int(values['cpf']))
                        break
            except Exception:
                self.__view.popUp()

    def delete(self, incidente: Incidente):
        if self.__dao_incidente.delete(incidente):
            return True
        else:
            return False

    def read(self, id: int):
        return self.__dao_incidente.read(id)