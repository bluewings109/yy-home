from yyhome.ports.inbound.elevator_port import ElevatorPort
from yyhome.ports.outbound.gayo_port import GayoPort


class ElevatorService(ElevatorPort):
    def __init__(self, gayo_port: GayoPort):
        self.gayo_port = gayo_port

    def call_elevator(self):
        self.gayo_port.call_elevator()
