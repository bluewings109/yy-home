from abc import ABC, abstractmethod

class GayoPort(ABC):

    @abstractmethod
    def refresh_token(self):
        pass

    @abstractmethod
    def call_elevator(self):
        pass
