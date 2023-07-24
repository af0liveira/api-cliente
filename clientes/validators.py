"""Implement field validators."""

import re

def cpf_is_valid(cpf_number):
    """Check if CPF has the correct number of digits."""
    return len(cpf_number) == 11

def nome_is_valid(nome):
    """Check whether `nome` points to a valid name."""
    return nome.replace(' ', '').replace('-', '').isalpha()

def rg_is_valid(rg_number):
    """Check whether RG has the correct number of digits."""
    return len(rg_number) == 9

def celular_is_valid(celular_number):
    """Validate cell phone number."""
    PATTERN = '\([1-9]{2}\)9[0-9]{4}-[0-9]{4}'
    result = re.findall(PATTERN, celular_number)
    return result