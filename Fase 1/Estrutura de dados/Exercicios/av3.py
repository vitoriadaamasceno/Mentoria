'''
📘 Atividade 3: Fatorial Recursivo e Validação de Entrada
🧩 Problema

Crie um programa que leia um número inteiro n (positivo) e:

    Valide se n é maior que zero.

    Calcule o fatorial de n usando recursão.

    Exiba o resultado formatado.

'''


def fatorial(numero):
    #primeiro a condição de parada
    if numero < 2:
        return 1
    return numero * fatorial(numero-1)

print(fatorial(5)) 