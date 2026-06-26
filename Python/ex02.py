"""Defina a função descendentes que pega uma árvore genealógica e retorna todos os descendentes da raiz. Utilize compreensões."""

def descendentes(arvore_genealogica):

    filhos = arvore_genealogica[1]
    
    nomes_filhos = [f[0] for f in filhos]
    
    nomes_netos = [neto for f in filhos for neto in descendentes(f)]
    
    return nomes_filhos + nomes_netos


arvore = ("João", [
    ("Maria", [
        ("Ana", []),
        ("Pedro", [])
    ]),
    ("Carlos", [])
])

print(descendentes(arvore))
