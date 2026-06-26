"""Dada uma lista com as notas de todos os alunos de uma turma, retorne a quantidade de alunos acima da média, que é 5"""

def contar_alunos_aprovados(notas_turma):

    return len([nota for nota in notas_turma if nota > 5])

historico_notas = [7.5, 4.0, 8.2, 3.5, 6.0, 5.0, 9.1, 2.8, 5.5]

print(contar_alunos_aprovados(historico_notas))