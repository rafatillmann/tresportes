
class Session():

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user
