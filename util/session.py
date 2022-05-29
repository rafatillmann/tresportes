
class Session():

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type


Session = Session()
