def eh_primo(numero):
    """Função auxiliar que verifica se um único número é primo."""
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def listar_primos_ate_100():
    """Função que percorre de 1 a 100 e gera a lista de números primos."""
    primos = []
    for num in range(1, 101):
        if eh_primo(num):
            primos.append(num)
    return primos


# Chamada da função e exibição dos resultados
resultado = listar_primos_ate_100()

print("Números primos entre 1 e 100:")
print(resultado)
print(f"\nTotal de números primos encontrados: {len(resultado)}")