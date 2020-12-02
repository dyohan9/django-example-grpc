from uuid import uuid4

from django.db import models


class Cliente(models.Model):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("-", "Prefiro não dizer"),
    ]
    cd_cliente = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column="cd_cliente",
    )
    nome = models.CharField("Nome", max_length=30)
    sobrenome = models.CharField("Sobrenome", max_length=50)
    cpf = models.CharField("CPF", max_length=14)
    sexo = models.CharField(
        "Sexo",
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True,
        null=False,
    )
