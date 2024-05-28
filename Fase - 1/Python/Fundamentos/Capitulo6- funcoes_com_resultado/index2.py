def fatorial(n):
    if not isinstance(n, int):
        print('Valor não é um numero inteiro')
        return None
    elif n < 0:
        print('Valor não pode ser um numero negativo')
        return None
    elif n == 0:
        return 1
    else:
        return n * fatorial(n-1)

while True:
    try:
        user_input = int(input("Digite um número inteiro: "))
        resultado = fatorial(user_input)
        if resultado is not None:
            print(f"Fatorial de {user_input} é {resultado}")
            break  # Saia do loop se o cálculo for bem-sucedido
    except ValueError:
        print('Por favor, digite um número inteiro válido')

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(2))