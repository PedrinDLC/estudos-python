"""
14) Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
"""

numeros = []
dicionario = {}

for n in range(5):
    valor = int(input(f'Digite o {n+1}º valor: '))
    numeros.append(valor)

    contagem = numeros.count(valor)
    dicionario[f'{valor}'] = contagem

print(f'\nNúmeros iguais: ')

for chave in dicionario:
    if dicionario.get(chave) > 1:
        print(f'{chave}: {dicionario.get(chave)} ocorrências')
