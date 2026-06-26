"""Gere uma lista contendo o tamanho de cada palavra. Ex de entrada: ["python", "java", "javascript", "c"]"""

def mapear_tamanho_palavras(lista_termos):

    return [len(termo) for termo in lista_termos]

dados_exemplo = ["python", "java", "javascript", "php", "c"]

print(mapear_tamanho_palavras(dados_exemplo))