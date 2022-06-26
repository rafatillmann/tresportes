from util.utils import cpf_validate, email_validate, generate_random_password
from view.viewCarga import ViewCarga
from dao.daoCarga import DaoCarga
from dao.daoCategoria import DaoCategoria
from dao.daoDestinatario import DaoDestinatario
from model.carga import Carga


class ControllerCarga():

    def __init__(self, session):
        self.__dao_carga = DaoCarga
        self.__dao_categoria = DaoCategoria
        self.__dao_destinatario = DaoDestinatario
        self.__view = ViewCarga()
        self.__session = session

    def options(self):
        while True:
            list = self.__dao_carga.list()
            button, values = self.__view.options(list)
            if not self.__session.menu(button):
                if button == 'insert':
                    self.insert()
                elif 'edit' in button:
                    route = self.__dao_carga.read(int(button.split(':')[1]))
                    self.edit(route)
                elif button == 'finish':
                    self.finish()

    def insert(self):
        while True:
            try:
                button, values = self.__view.inicial()
                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'save':
                        destinatario = self.__dao_destinatario.read(values['cpf'])
                        carga = Carga(values['categoria'], values['altura'], values['largura'], values['comprimento'],
                                            values['peso'], values['descricao'], values['cpf'], '123', 'Não alocada')
                        self.__dao_carga.insert(carga)
                        break
            except Exception:
                self.__view.popUp()

    def update(self, carga: Carga):
        pass

    def delete(self, carga: Carga):
        if self.__dao_carga.delete(carga):
            return True
        else:
            return False

    def read(self, id: int):
        return self.__dao_carga.read(id)

    def read_unused(self):
        return self.__dao_carga.read_unused()

    def read_by_route(self, route_id):
        return self.__dao_carga.read_by_route(route_id)
