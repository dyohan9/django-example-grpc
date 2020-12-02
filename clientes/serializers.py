from django_grpc_framework import proto_serializers
from clientes.models import Cliente
from cliente_proto import cliente_pb2


class ClienteProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Cliente
        proto_class = cliente_pb2.Cliente
        fields = ["cd_cliente", "nome", "sobrenome", "cpf", "sexo"]
