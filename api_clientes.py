import grpc
from cliente_proto import cliente_pb2, cliente_pb2_grpc


with grpc.insecure_channel("localhost:50051") as channel:
    stub = cliente_pb2_grpc.ClienteControllerStub(channel)
    print("----- Create -----")
    response = stub.Create(
        cliente_pb2.Cliente(
            nome="Daniel", sobrenome="Yohan", cpf="00000000001", sexo="M"
        )
    )
    print(response, end="")

    print("----- List -----")
    for cliente in stub.List(cliente_pb2.Cliente()):
        print(cliente.cpf)
        print(cliente, end="")

    print("----- Retrieve -----")
    response = stub.Retrieve(
        cliente_pb2.Cliente(cd_cliente=response.cd_cliente)
    )
    print(response, end="")

    print("----- Update -----")
    response = stub.Update(
        cliente_pb2.Cliente(
            cd_cliente=response.cd_cliente,
            nome="Daniel do GRPC",
            sobrenome="Baptista",
            cpf="11111111111",
            sexo="M",
        )
    )
    print(response, end="")

    # print("----- Delete -----")
    # stub.Destroy(cliente_pb2.Cliente(cd_cliente="388783d1-4ca5-4841-9557-6091077994de"))
