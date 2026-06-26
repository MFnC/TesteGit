"""Considere listas de listas e números. Cada lista, por sua vez, está formada por listas e números, recursivamente.
Defina uma função achatar que retorne uma lista plana com todos os números da lista original.
Por exemplo, achatar([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]) deverá retornar [1, 2, 4, 2, 5, 2, 1, 2, 3, 1, 8].
Dê duas versões, uma sem compreensões e outra com compreensões. 
A versão com compreensões não precisa retornar os elementos na ordem em que aparecem os números de esquerda à direita."""

#Sem compreensão

def achatar(lista_complicada):

    resultado = []
    
    if type(lista_complicada) != list:
        return [lista_complicada]
        
    for elemento in lista_complicada:
        lista_achatada = achatar(elemento)
        resultado.extend(lista_achatada)
        
    return resultado

print(achatar([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]))

#Com compreensão

def achatar_compreensao(dados):

    if type(dados) is not list:
        return [dados]
        
    return [numero for sub_item in dados for numero in achatar_compreensao(sub_item)]

print(achatar_compreensao([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]))
