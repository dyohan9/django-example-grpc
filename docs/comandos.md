## Gerar `cliente.proto`

```
python manage.py generateproto --model clientes.models.Cliente --fields=cd_cliente,nome,sobrenome,cpf,sexo --file protos/cliente_proto/cliente.proto

```

# Para atualizar o código grpc utilizado por nossa aplicação para usar uma nova #definição de serviço é necessário rodar o comando abaixo
```
python -m grpc_tools.protoc --proto_path=./protos --python_out=./ --grpc_python_out=./ ./protos/cliente_proto/cliente.proto
```
