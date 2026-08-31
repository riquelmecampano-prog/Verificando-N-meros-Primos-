# 1. Função simples de soma
def somar(a, b):
    return a + b

# Exemplo de uso:
resultado_soma = somar(5, 3)
print(f"Soma simples: {resultado_soma}")


# 2. Função calculadora para as 4 operações
def calcular(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
        nome_operacao = "SOMA"
    elif operacao == 2:
        resultado = num1 - num2
        nome_operacao = "SUBTRAÇÃO"
    elif operacao == 3:
        resultado = num1 * num2
        nome_operacao = "MULTIPLICAÇÃO"
    elif operacao == 4:
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        resultado = num1 / num2
        nome_operacao = "DIVISÃO"
    else:
        return "Erro: Operação inválida. Escolha um número de 1 a 4."

    return f"O RESULTADO DA {nome_operacao} É : {resultado}"

# Exemplos de uso da função calculadora:
print(calcular(10, 5, 1))  # Soma
print(calcular(10, 5, 2))  # Subtração
print(calcular(10, 5, 3))  # Multiplicação
print(calcular(10, 5, 4))  # Divisão