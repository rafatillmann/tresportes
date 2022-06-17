from controller.controllerMotorista import ControllerMotorista


class ControllerSession():

    def __init__(self):
        self.__controller_motorista = ControllerMotorista(self)

    def menu(self, button):

        if button == None:
            exit()
        elif button == 'route':
            pass
        elif button == 'driver':
            self.__controller_motorista.options()
        elif button == 'load':
            pass
        else:
            return False

    def session_manager(self):
        while True:
            self.__controller_motorista.options()

    def session_driver(self):
        pass

    def session_receiver(self):
        pass
