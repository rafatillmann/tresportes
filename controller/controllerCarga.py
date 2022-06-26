from util.utils import cpf_validate, email_validate, generate_random_password
from view.viewCadastroCarga import ViewCadastroCarga
from dao.daoCarga import DaoCarga
from model.carga import Carga


class ControllerCarga():

    def __init__(self, session):
        self.__dao_carga = DaoCarga
        self.__view = ViewCadastroCarga()
        self.__session = session

    def options(self):
        pass

    def insert(self):
        pass

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


