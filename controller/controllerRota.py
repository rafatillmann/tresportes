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
            button, values = self.__view.display()
            if not self.__session.menu(button):
                if button == 'cancel':
                    break
                elif button == 'save':
                    pass

    def finish(self):
        pass
