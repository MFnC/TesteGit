"""Contar quantidade de vogais em uma string"""

def computar_total_vogais(texto):

    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    return sum(1 for caractere in texto if caractere in vogais)

entrada_usuario = input("Digite uma frase: ")
print(computar_total_vogais(entrada_usuario))