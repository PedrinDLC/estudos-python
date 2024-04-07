num = []

for i in range(8):
    num.append(int(input(f'Digite o {i+1}° número: ')))

x = int(input('Informe a posição x: ')) - 1
while True:
    if -1 < x < 8:
        break
    else:
        x = int(input('Posição inválida! Tente Novamente.\nInforme a posição x: ')) - 1
y = int(input('Informe a posição y: ')) - 1
while True:
    if -1 < y < 8:
        break
    else:
        y = int(input('Posição inválida! Tente Novamente.\nInforme a posição y: ')) - 1

soma = num[x] + num[y]

print(f'Soma das posições {x+1} e {y+1}: {soma}')
