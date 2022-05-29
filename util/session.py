
class Session():

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: int):
        self.__tipo = tipo


Session = Session()
