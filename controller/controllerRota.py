from dao.daoRota import DaoRota
from view.viewRota import ViewRota


class ControllerRota():

    def __init__(self, session):
        self.__view = ViewRota()
        self.__session = session
        self.__dao_rota = DaoRota

    def options(self):
        while True:
            list = self.__dao_rota.list()
            button, values = self.__view.options(list)
            if not self.__session.menu(button):
                if button == 'insert':
                    self.insert()
                elif button == 'edit':
                    break
                elif button == 'finish':
                    self.finish()

    def insert(self):
        while True:
            list_loads = [1, 2, 3, 4]
            button, values, loads = self.__view.display(list_loads)
            if not self.__session.menu(button):
                if button == 'cancel':
                    break
                elif button == 'save':
                    if loads:
                        self.add(loads)
                    else:
                        break

    def finish(self):
        pass

    def add(self, values):
        pass
