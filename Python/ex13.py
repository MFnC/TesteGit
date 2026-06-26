"""Dada uma matriz de inteiros, me faça uma lista com apenas os numeros pares da matriz"""

def isolar_pares_matriz(matriz_dados):

    return [numero for linha in matriz_dados for numero in linha if numero % 2 == 0]

minha_matriz = [
    [12, 7, 22, 15],
    [3, 44, 18, 9]
]

print(isolar_pares_matriz(minha_matriz))
