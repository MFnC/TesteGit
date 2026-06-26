"""Faça uma lista com os números pares de uma lista de inteiros"""

def filtrar_valores_pares(colecao_numeros):

    return [num for num in colecao_numeros if num % 2 == 0]

dados_num = [14, 23, 32, 45, 58, 61, 70, 89, 92]

print(filtrar_valores_pares(dados_num))
