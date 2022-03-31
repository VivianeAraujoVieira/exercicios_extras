"""Refazer o desafio da tabuada, 
utilizando o laço for, com o numero que o usuario escolher"""

num = int(input("Digite um número: ")) 
for c in range(0,1 + 1):
    print(f"\n{num} * {c}  = {num*c}")
    c=c+1
print(c)


    
