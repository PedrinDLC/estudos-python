vetor = []

for n in range(20):
    num = int(input(f'Digite o {n+1}º numero: '))
    if num not in vetor:
        vetor.append(num)

print(vetor)
