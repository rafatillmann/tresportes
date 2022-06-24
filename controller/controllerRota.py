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
            button, values = self.__view.inicial()
            if not self.__session.menu(button):
                if button == 'cancel':
                    break
                elif button == 'add':
                    self.add()

    def edit(self, values):
        while True:
            button, values = self.__view.edit()
            if not self.__session.menu(button):
                pass

    def finish(self):
        pass

    def add(self):
        while True:
            button, values = self.__view.select_load([1, 2, 3])
            if not self.__session.menu(button):
                if button == 'back':
                    break
                elif button == 'sel':
                    pass
                    # for por cada carga capturando o endereço e criando um array de endereços
                    # enviar para o request
                    # somar o tempo de todos e criar uma rota, ver método que pega último registro no banco
                    # for em cada resposta e criando os pontos e logo em seguida preenche o percurso
                    # for pontos percurso pontoA recebe atual e B o próximo, analisar questão do primeiro ponto
                    # chada tela edit enviando o id da nova rota

                    # ver de criar dois add ou ele recebe id rota e atualiza quaso tenha id
