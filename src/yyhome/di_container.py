from dependency_injector import containers

class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["yyhome.adapter.inbound.api"])
