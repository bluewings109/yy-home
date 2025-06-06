from dependency_injector import containers
from dependency_injector import providers

from yyhome.adapters.outbound.external_api.gayo_client import GayoClient
from yyhome.application.service.elevator_service import ElevatorService
from yyhome.config.settings import Settings


class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["yyhome.adapters.inbound.http.routers.v1.elevator_router"])

    # settings
    settings = providers.Singleton(Settings)

    # client
    gayo_client = providers.Singleton(GayoClient, settings=settings)

    # service
    elevator_service = providers.Singleton(ElevatorService, gayo_port=gayo_client)
