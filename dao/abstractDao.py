from abc import ABC, abstractmethod


class AbstractDao(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def populate(self):
        pass