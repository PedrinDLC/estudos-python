maior = menor = 0
num = []

for i in range(10):
    num.append(int(input(f'Digite o {i+1}° número: ')))

for n in range(10):
    if n == 0:
        maior = menor = num[n]
    elif num[n] > maior:
        maior = num[n]
    elif num[n] < menor:
        menor = num[n]

print(f'Maior: {maior}')
print(f'Menor: {menor}')
