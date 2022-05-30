from random import randint
from model.destinatario import Destinatario
from dao.daoDestinatario import DaoDestinatario
from view.viewCadastroDestinatario import ViewDestinatario 


class ControllerDestinatario:
    
    def __init__(self):
        self.__dao_destinatario = DaoDestinatario
        self.__view = ViewDestinatario()
        
    def options(self):
        pass
            
    def insert (self, email: str = None):
       try:
           if email:
               destinatario = self.__dao_destinatario.readByEmail(email)
               button, values = self.__view.display(destinatario)
           else:
               button, values = self.__view.display()
           
           if button == 'save':               
               destinatario = Destinatario(values['nome'], values['email'],values['cpf'], values['senha'], values['cpf'], values['endereco'], values['complemento'], values['telefone'])
               
               self.__dao_destinatario.insert(destinatario)

           
       except Exception:
           pass    
          
 
    
    def update(self):
        pass    
    
    def delete(self):
        pass
    
    def read(self, id: int):
        return self.__dao_destinatario.read(id)