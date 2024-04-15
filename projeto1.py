# PROJETO 1

# estamos criando um modulo de login do nosso aplicativo, e voce deve obter as seguintes informações do usuário

"""
MODULO 1 - GERAR REGISTRO DO FUNCIONÁRIO

Funcionalidades do Módulo 1

- Obtenha o nome do usuário
- Obtenha a idade do usuário
- Registre de forma automática a data do cadastro do usuário
- Para cada novo funcionário q é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória
 cartões = ["R$50,00", "R$250,00", "R$120,00"]
- guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
"""
from datetime import datetime
import random

nome = str(input('Digite seu nome: '))
data_nasc = datetime.strptime(
    input('Digite sua data de nascimento: (dd/mm/aaaa) '), '%d/%m/%Y')
idade = datetime.now().year - data_nasc.year
data_cadastro = datetime.now()

cartoes = [250.0, 120.0, 50.0]
sorteio = random.choice(cartoes)

"""
MODULO 2 - GERAR APRESENTAÇÃO DO USUÁRIO

# Funcionalidades do Módulo 2 - Mensagem de boas vindas

usando os dados obtidos no modulo 1, exiba as seguintes informações:
- Olá (nome do usuário), seu registro foi concluido com sucesso no dia(data de cadastro no 
dia dd/mm/aaaa).
Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado)
"""

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {
      data_cadastro.date()}.')
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de R${
      sorteio:.2f}')
