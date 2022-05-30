from controller.controllerMotorista import ControllerMotorista
from view.viewLogin import ViewLogin
from controller.controllerUsuario import ControllerUsuario
from controller.controllerDestinatario import ControllerDestinatario
from util.session import Session


class Login():
    def __init__(self):
        self.__controller_usuario = ControllerUsuario()
        self.__controller_destinatario = ControllerDestinatario()
        self.__view = ViewLogin()

    def start(self):
        try:
            button, values = self.__view.login()
            if button == 'save':
                email = values['email']
                senha = values['senha']
                if email and senha:
                    login = self.__controller_usuario.login(email, senha)
                    if login:
                        self.app(email)
                    else:
                        pass
            elif button == 'insert':
                self.__controller_destinatario.insert()

        except Exception:
            pass

    def app(self, email: str = None):
        if Session.type == 'Motorista':
            pass
        elif Session.type == 'Gerente':
            while True:
                ControllerMotorista().options()
        elif Session.type == 'Destinatario':
            while True:
                ControllerDestinatario().update(email)
        else:
            pass
