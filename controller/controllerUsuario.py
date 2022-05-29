
class controllerUsuario():

    def __init__(self):
        self.__daoDestinatario = None
        self.__daoGerente = None
        self.__daoMotorista = None
        self.__view = None  

    def login(self, email: str, password: str):
        try:
            if isinstance(email, str) and isinstance(password, str):
                user = self.__daoDestinatario.readByEmail(email)
                
                if(not user):
                    user = self.__daoGerente.readByEmail(email)
                if(not user):
                    user = self.__daoMotorista.readByEmail(email)
                    
                if(user):
                    if(user.password == password):
                        return True
                return False
        except Exception:
            pass