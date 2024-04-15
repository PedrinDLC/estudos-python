# DESAFIO

import random

""" Desafios Random 
1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa jogue as opções dentro de uma variável e depois crie um programa que imprimir "cara" ou "coroa" na tela  """

moeda = random.choice(['Cara', 'Coroa'])
print(moeda)

""" 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela  """

nomes = ['Lucas', 'Mateus', 'Otavio', 'Ana', 'Jéssica']

escolha = random.choice(nomes)

print(f'O sorteado foi {escolha}')

""" 3. Você quer escolher aleatoriamente um número de 10-100 Imprima na tela um valor aleatório entre 10 e 100 """

print(random.randint(10, 100))
