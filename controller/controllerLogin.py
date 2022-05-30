from view.viewLogin import ViewLogin
from controller.controllerUsuario import ControllerUsuario
from util.session import Session

class Login():
    def __init__(self):
        self.__controller_usuario = ControllerUsuario()
        self.__view = ViewLogin()

    def start(self):
        try:
            email, senha = self.__view.login()
            if email and senha:
                login = self.__controller_usuario.login(email, senha)
                if login:
                    type = Session.type
                    print(type)
                else:
                    pass
        except Exception:
            pass