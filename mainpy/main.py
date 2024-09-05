import math

def is_prime(num):
    """Verifica se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci_up_to(n):
    """Gera números de Fibonacci até o valor n."""
    fib_sequence = [0, 1]
    while fib_sequence[-1] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def matriz_vinhos(rows, cols):
    """Cria a matriz de vinhos."""
    # Limite baseado no maior índice possível na matriz
    max_value = rows + cols
    
    # Gerar números de Fibonacci até o maior valor de i + j possível
    fibonacci_numbers = set(fibonacci_up_to(max_value))
    
    # Criar a matriz
    matriz = [['' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            soma = i + j
            # Verificar se a soma é tanto um número de Fibonacci quanto primo
            if soma in fibonacci_numbers and is_prime(soma):
                matriz[i][j] = 'Vinho'  # Coloca vinho naquela célula
            else:
                matriz[i][j] = ''  # Deixa vazio ou outro valor
        
    return matriz

# Exemplo de uso
rows = 10
cols = 10
matriz = matriz_vinhos(rows, cols)

# Exibir matriz
for row in matriz:
    print(row)
