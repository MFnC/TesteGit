"""Crie uma lista com todos os números primos de 1 a n"""

def verificar_se_e_primo(numero):

    if numero <= 1:
        return False

    return all(numero % divisor != 0 for divisor in range(2, numero))

def gerar_primos_ate_n(limite):

    return [num for num in range(1, limite + 1) if verificar_se_e_primo(num)]

valor_usuario = int(input("Digite o valor de n: "))
print(gerar_primos_ate_n(valor_usuario))