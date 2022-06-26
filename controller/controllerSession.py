from controller.controllerMotorista import ControllerMotorista
from controller.controllerRota import ControllerRota
from controller.controllerCarga import ControllerCarga


class ControllerSession():

    def __init__(self):
        self.__controller_motorista = ControllerMotorista(self)
        self.__controller_rota = ControllerRota(self)
        self.__controller_carga = ControllerCarga(self)

    def menu(self, button):

        if button == None:
            exit()
        elif button == 'route':
            self.__controller_rota.options()
        elif button == 'driver':
            self.__controller_motorista.options()
        elif button == 'load':
            self.__controller_carga.options()
        else:
            return False

    def session_manager(self):
        while True:
            self.__controller_rota.options()

    def session_driver(self):
        pass

    def session_receiver(self):
        pass
