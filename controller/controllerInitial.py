from view.viewInitial import ViewInitial
from controller.controllerUsuario import ControllerUsuario

class Initial():
    def __init__(self):
        self.__controller_usuario = ControllerUsuario()
        self.__view = ViewInitial()

    def start(self):
        try:
            email, password = self.__view.login()
            if email and password:
                login = self.__controller_usuario.login(email, password)
                if login:
                    self.options()
                else:
                    pass
        except Exception:
            pass