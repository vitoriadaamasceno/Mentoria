""" from typing import Callable


def nova_funcao(nome: str) -> str:
    # Aqui temos um "caso base"
    # A função retorna um valor
    return f'Oi, {nome}!'


def funcao_anterior(nome: str, funcao: Callable) -> str:
    # Aqui o código pausa e vai até
    # nova_funcao
    return funcao(nome)


nome = 'Luiz'
# Aqui o código pausa
# e vai até a funcao_anterior
frase = funcao_anterior(nome, nova_funcao)
# Aqui o código
# continua seu fluxo
print(frase)  # Oi, Luiz! """
import sys
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())  # 5000

def fatorial(n: int) -> int:
  if n == 1 or n == 0:
      return 1
  return n * fatorial(n - 1)


if __name__ == "__main__":
  fat5 = fatorial(998)
  print(fat5)