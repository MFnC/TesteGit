"""Defina uma função que leia do teclado uma sequência de números inteiros dados em uma única linha.
A função deve retornar uma lista contendo os números que estão na linha."""

def teclado ():
    entrada = input().split()
    lista_inteiros = [int(item) for item in entrada]
    return lista_inteiros

print(teclado())