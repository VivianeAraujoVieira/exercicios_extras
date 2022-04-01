
"""Crie um programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
atual = date.today().year
total_menor = 0
total_maior = 0
for pess in range(1, 8):
    data = int(input(f"Olá! Por favor, informe data de nascimento da {pess}ª pessoa: "))
    idade = atual - data
    if idade <=18:
        total_menor += 1
    else: 
        total_maior +=1
print(f"Ao todo tivemos {total_maior} pessoas maiores de idade")
print(f"E {total_menor} menores de idade")
        
    

        
    
        