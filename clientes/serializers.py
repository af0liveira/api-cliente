from rest_framework import serializers

from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        """Validate Cliente data."""

        errors = {}

        if not cpf_is_valid(data['cpf']):
            errors['cpf'] = "O número informado não é um CPF válido."

        if not nome_is_valid(data['nome']):
            errors['nome'] = "Este campo só pode conter letras, espaços e hífens."

        if not rg_is_valid(data['rg']):
            errors['rg'] = "Este campo deve ter 9 dígitos."

        if not celular_is_valid(data['celular']):
            errors['celular'] = "Deve obedecer o padrão '(xx)9yyyy-zzzz'."

        if errors:
             raise serializers.ValidationError(errors)

        return data