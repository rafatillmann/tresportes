from dao.daoCarga import DaoCarga
from dao.daoCategoria import DaoCategoria
from model.destinatario import Destinatario
from util.utils import cpf_validate, email_validate, generate_random_password
from view.viewCarga import ViewCarga

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
                    carga = self.__dao_carga.read(int(button.split(':')[1]))
                    self.update(carga)

    def insert(self):
        while True:
            try:
                button, values = self.__view.inicial()
                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'save':
                        destinatario = self.__dao_destinatario.readByCPF(
                            int(values['cpf']))
                        categoria = self.__dao_categoria.read_by_name(
                            values['categoria'])

                        carga = Carga(categoria, values['altura'], values['largura'], values['comprimento'],
                                      values['peso'], values['descricao'], destinatario, None, 'Não alocada')
                        self.__dao_carga.insert(carga)
                        break
            except Exception:
                self.__view.popUp()

    def update(self, carga: Carga):
        while True:
            try:
                button, values = self.__view.edit(carga)
                if not self.__session.menu(button):
                    if button == 'cancel':
                        break
                    elif button == 'save':
                        break
            except Exception:
                self.__view.popUp()

    def delete(self, carga: Carga):
        if self.__dao_carga.delete(carga):
            return True
        else:
            return False

    def read(self, id: int):
        return self.__dao_carga.read(id)

    def read_unused(self):
        return self.__dao_carga.read_unused()

    def read_by_route(self, route):
        return self.__dao_carga.read_by_route(route)

    def update_carga(self, carga: Carga):
        return self.__dao_carga.update(carga)
