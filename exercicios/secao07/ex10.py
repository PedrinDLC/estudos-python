notas = []

for i in range(15):
    notas.append(float(input(f'Digite a nota do {i+1}° aluno: ')))

media = sum(notas) / len(notas)
print(f'Média geral: {media}')
