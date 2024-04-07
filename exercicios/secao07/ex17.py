numeros = []

for n in range(10):
    numeros.append(int(input(f'Digite o {n+1}º numero: ')))
    if numeros[n] < 0:
        numeros[n] = 0

print(numeros)
