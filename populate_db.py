"""Script to generate test entries for the project's database."""

import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF

from clientes.models import Cliente


def create_clientes(num_clientes):
    fake = Faker('pt_BR')
    Faker.seed(10)

    for _ in range(num_clientes):
        cpf = CPF().generate()
        nome = fake.name()
        email_user = nome.replace(' ', '').lower()
        email_domain = fake.free_email_domain()
        email = f'{email_user}@{email_domain}'
        rg = (f'{random.randrange(10, 99):02d}'
              f'{random.randrange(100, 999):03d}'
              f'{random.randrange(100, 999):03d}'
              f'{random.randrange(0, 9):1d}')
        celular = (f'({random.randrange(10, 40):02d})'
                   f'9{random.randrange(4000, 9999):04d}'
                   f'-{random.randrange(4000, 9999):04d}')
        ativo = random.choice([True, False])
        cliente = Cliente(nome=nome, email=email, cpf=cpf, rg=rg,
                          celular=celular, ativo=ativo)
        cliente.save()


if __name__ == '__main__':
    try:
        create_clientes(50)
    except Exception:
        raise
    else:
        print("Database successfully populated.")
