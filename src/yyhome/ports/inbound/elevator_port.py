from abc import ABC, abstractmethod

class ElevatorPort(ABC):
    @abstractmethod
    def call_elevator(self):
        pass
