import string

# Abrir o arquivo
fin = open('livro.txt')

# Inicializar o dicionário para contagem de palavras
word_count = {}

# Processar cada linha do arquivo
for line in fin:
    if line.strip():  # Verificar se a linha não está vazia
        words = line.split()  # Dividir a linha em palavras
        for word in words:
            word = word.translate(str.maketrans('', '', string.punctuation))  # Remover pontuação
            word = word.lower()  # Converter para minúsculas
            
            # Atualizar o dicionário de contagem de palavras
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# Fechar o arquivo
fin.close()

# Obter a lista de palavras únicas
lista_palavras_unicas = list(word_count.keys())

# Ordenar o dicionário pela contagem das palavras
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# Selecionar as 20 palavras mais frequentes
top_20_words = sorted_word_count[:20]

# Exibir os resultados
print(f'Total de palavras únicas: {len(lista_palavras_unicas)}')
print('As 20 palavras mais frequentes são:')
for word, count in top_20_words:
    print(f'{word}: {count}')
