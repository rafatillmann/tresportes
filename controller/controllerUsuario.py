from util.session import Session
from dao.daoDestinatario import DaoDestinatario
from dao.daoGerente import DaoGerente
from dao.daoMotorista import DaoMotorista


class ControllerUsuario():

    def __init__(self):
        self.__daoDestinatario = DaoDestinatario
        self.__daoGerente = DaoGerente
        self.__daoMotorista = DaoMotorista

    def login(self, email: str, senha: str):
        try:
            user = self.__daoDestinatario.readByEmail(email)
            type = "Destinatario"

            if(not user):
                user = self.__daoGerente.readByEmail(email)
                type = "Gerente"
            if(not user):
                user = self.__daoMotorista.readByEmail(email)
                type = "Motorista"

            if(user):
                if(user.senha == senha):
                    Session.type = type
                    Session.user = user
                    return True

            return False
        except Exception:
            pass
