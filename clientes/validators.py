"""Implement field validators."""

def cpf_is_valid(cpf_number):
    """Check if CPF has the correct number of digits."""
    return len(cpf_number) == 11

def nome_is_valid(nome):
    """Check whether `nome` points to a valid name."""
    return nome.replace(' ', '').replace('-', '').isalpha()

def rg_is_valid(rg_number):
    """Check whether RG has the correct number of digits."""
    return len(rg_number) == 9

def celular_is_valid(cel_number):
    """Validate celular number."""
    return len(cel_number) >= 11