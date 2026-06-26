"""Dada uma lista com nomes, filtrar palavras maiores que 5 letras"""

def obter_palavras_longas(lista_palavras):

    return [palavra for palavra in lista_palavras if len(palavra) > 5]

elementos = ['Computador', 'Uva', 'Programador', 'Python', 'Mesa', 'Teclado', 'Cadeira']
print(obter_palavras_longas(elementos))
