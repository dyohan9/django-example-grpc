import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from clientes.models import Cliente
from clientes.serializers import ClienteProtoSerializer


class ClienteService(Service):
    def List(self, request, context):
        clientes = Cliente.objects.all()
        print(clientes)
        serializer = ClienteProtoSerializer(clientes, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = ClienteProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, "Cliente:%s not found!" % pk)

    def Retrieve(self, request, context):
        cliente = self.get_object(request.cd_cliente)
        serializer = ClienteProtoSerializer(cliente)
        return serializer.message

    def Update(self, request, context):
        cliente = self.get_object(request.cd_cliente)
        serializer = ClienteProtoSerializer(cliente, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        cliente = self.get_object(request.cd_cliente)
        cliente.delete()
        return empty_pb2.Empty()
