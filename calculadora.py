def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de b de a."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b. Lança ValueError se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
