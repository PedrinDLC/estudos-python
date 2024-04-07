numeros = []

for n in range(5):
    numeros.append(int(input(f'Digite o {n+1}º numero: ')))

while True:
    print('-='*20)
    print('[ 0 ] - Sair')
    print('[ 1 ] - Ver vetor')
    print('[ 2 ] - Vetor invertido')
    print('-='*20)
    op = int(input('Digite uma opção: '))
    if op == 0:
        break
    elif op == 1:
        print(numeros)
    elif op == 2:
        print(numeros[::-1])
    else:
        print('Opção inválida! Tente novamente!')
        