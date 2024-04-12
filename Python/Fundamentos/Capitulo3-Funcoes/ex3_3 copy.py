#segunda alternativa

def desenha_grade(n):
    for i in range(n):
        # Desenha a linha superior da célula
        print('+', end=' ')
        print('- ' * n, end='')
        print('+', end=' ')
        print('- ' * n, end='')
        print('+')

        # Desenha as linhas internas da célula
        for j in range(n):
            print('|', end=' ')
            print(' ' * n*2, end='')
            print('|', end=' ')
            print(' ' * n*2, end='')
            print('|')

    # Desenha a última linha inferior da célula
    print('+', end=' ')
    print('- ' * n, end='')
    print('+', end=' ')
    print('- ' * n, end='')
    print('+')

# Chamada da função para desenhar a grade
desenha_grade(10)
