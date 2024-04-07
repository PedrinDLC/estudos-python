num = []

for i in range(6):
    num.append(int(input(f'Digite o {i+1}° número par: ')))
    while True:
        if num[i] % 2 == 0:
            break
        else:
            num[i] = int(input(f'Tente novamente! Digite o {i + 1}° número par: '))

print(num)
print(num[::-1])
