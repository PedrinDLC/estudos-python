numeros = []
maior = menor = media = 0

for n in range(5):
    numeros.append(int(input(f"Digite o {n + 1}º número: ")))
    if n == 0:
        maior = numeros[n]
        menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        elif numeros[n] < menor:
            menor = numeros[n]

media = sum(numeros) / len(numeros)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Media: {media}')
