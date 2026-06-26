"""Crie uma lista que que extraia todas as letras das palavras e gere uma única lista.
 Ex: palavras = ["python", "java"]. Saída = ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a']"""

def unificar_letras(lista_palavras):

    return [caractere for palavra in lista_palavras for caractere in palavra]

termos_teste = ["html", "linux", "git"]

print(unificar_letras(termos_teste))
