"""Dada uma lista numérica, retorne apenas os números positivos"""

def extrair_positivos(lista_numeros):

    return [valor for valor in lista_numeros if valor > 0]

valores_teste = [12, -5, 0, -1, 8, -22, 4, -3]

print(extrair_positivos(valores_teste))
