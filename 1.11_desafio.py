
"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do porogama, mostre:

A média de idade do grupo;
Qual o nome do homem mais velho;
Quantas mulheres tem menos de 20 anos. """
soma_idade = 0
media_idade = 0
maior_idade =0
nome_velho = ''
tot_mulher20 = 0
for p in range(1, 5):
    pessoas = input(f"-------{p}ª PESSOA---------")
    nome = input("NOME: ")
    idade = int(input("IDADE: "))
    sexo = input("SEXO [F/M]: ")
    soma_idade += idade
    if p == 1 and sexo in "Mm" :
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mn' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

    

media_idade = soma_idade / 4
print(f"A média idade do grupo é de {media_idade} anos")
print(f"O homem mais velho tem {maior_idade} anos e se chama {nome_velho} ")
print(f"Total de mulheres no grupo com menos de 20 anos é {tot_mulher20}")
    



    
