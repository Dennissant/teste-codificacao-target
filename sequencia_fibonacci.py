# sequencia_fibonacci.py
def pertence_fibonacci(numero):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    """
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

# Bloco opcional para execução direta
if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
