maior = pos = 0
num = []

for i in range(10):
    num.append(int(input(f'Digite o {i+1}° número: ')))

for n in range(10):
    if n == 0:
        maior = num[n]
        pos = n
    elif num[n] > maior:
        maior = num[n]
        pos = n

print(f'Vetor: {num}')
print(f'O maior elemento é {maior} e está na posição {pos}')
