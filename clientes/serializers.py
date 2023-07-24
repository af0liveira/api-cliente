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
            errors['cpf'] = "Este campo deve conter 11 dígitos."

        if not nome_is_valid(data['nome']):
            errors['nome'] = "Este campo só pode conter letras, espaços e hífens."

        if not rg_is_valid(data['rg']):
            errors['rg'] = "Este campo deve ter 9 dígitos."

        if not celular_is_valid(data['celular']):
            errors['celular'] = "Este campo deve ter no mínimo 11 dígitos."

        if errors:
             raise serializers.ValidationError(errors)

        return data