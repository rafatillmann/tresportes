from view.viewLogin import ViewLogin
from controller.controllerUsuario import ControllerUsuario
from util.session import Session

class Login():
    def __init__(self):
        self.__controller_usuario = ControllerUsuario()
        self.__view = ViewLogin()

    def start(self):
        try:
            email, password = self.__view.login()
            if email and password:
                login = self.__controller_usuario.login(email, password)

                if login:
                    pass
                else:
                    pass
        except Exception:
            pass