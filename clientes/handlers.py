from clientes.services import ClienteService
from cliente_proto import cliente_pb2_grpc


def grpc_handlers(server):
    cliente_pb2_grpc.add_ClienteControllerServicer_to_server(
        ClienteService.as_servicer(),
        server,
    )
