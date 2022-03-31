"""Refazer o desafio da tabuada, 
utilizando o laço for, com o numero que o usuario escolher"""

num = int(input("Digite um número: ")) 
for c in range(1, 11):
    print(f"{num} * {c:2}  = {num*c}")


    
