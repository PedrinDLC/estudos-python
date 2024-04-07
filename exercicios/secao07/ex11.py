numeros = []
negativos = somapositivos = 0

for n in range(10):
    numeros.append(int(input(f"Digite o {n+1}º número: ")))
    if numeros[n] < 0:
        negativos += 1
    else:
        somapositivos += numeros[n]


print(f'Quantidade de numeros negativos: {negativos}')
print(f'Soma dos positivos: {somapositivos}')
