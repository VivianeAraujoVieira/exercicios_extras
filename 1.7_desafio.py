
""" Faça um programa que leia um numero inteiro e diga se ele é ou não um número primo. """

n = int(input(' Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[33m ", end=' ')
        total += 1
    else:
        print("\033[31m ", end=' ') 

    print(' ',c, end=' ')

print (f"\n\033[mO número {n} foi divisivel {total} vezes")
if total == 2:
    print("Por tanto ele é um número primo! ")
else: 
    print("Por isso ele não é um número primo! ")