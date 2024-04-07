numeros = []
maior = menor = 0
posmaior = posmenor = 0
for n in range(5):
    numeros.append(int(input(f"Digite o {n + 1}º número: ")))
    if n == 0:
        maior = numeros[n]
        menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
            posmaior = n
        elif numeros[n] < menor:
            menor = numeros[n]
            posmenor = n

media = sum(numeros) / len(numeros)

print(f'Posição do maior: {posmaior}')
print(f'Posição do menor: {posmenor}')
