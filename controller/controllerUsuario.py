from util.session import Session

class ControllerUsuario():

    def __init__(self):
        self.__daoDestinatario = None
        self.__daoGerente = None
        self.__daoMotorista = None
        self.__view = None  

    def login(self, email: str, password: str):
        try:
            if isinstance(email, str) and isinstance(password, str):
                user = self.__daoDestinatario.readByEmail(email)
                type = "Destinatario"

                if(not user):
                    user = self.__daoGerente.readByEmail(email)
                    type = "Gerente"
                if(not user):
                    user = self.__daoMotorista.readByEmail(email)
                    type = "Motorista"
                    
                if(user):
                    if(user.password == password):
                        Session.type = type
                        return True
                return False
        except Exception:
            pass