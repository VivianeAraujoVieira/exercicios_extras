
"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
EX: 
    APOS A SOPA;
    A SACADA DA CASA;
    A TORRE DA DERROTA;
    ANOTARAM A DATA DA MARATONA;
    LOBO AMA BOLO;
    """

FRASE = str(input("Digite uma frase: ")).upper()
palavras = FRASE.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1): 
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
