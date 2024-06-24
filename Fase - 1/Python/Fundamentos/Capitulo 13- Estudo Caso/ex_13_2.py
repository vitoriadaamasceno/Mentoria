import string

#13.1
fin = open('livro.txt')
lista_palavras =[]
por_palavra = []
for line in fin:
    if line != '\n':
       line.strip()
       words = line.split()
       for word in words:
           word = word.translate(str.maketrans('','',string.punctuation)) #remove pontuação, usando a função translate que recebe um dicionário de tradução e remove a pontuação
           
           word = word.lower()
           lista_palavras.append(word)
           teste = {word: lista_palavras.count(word)}
           por_palavra.append(teste)
           
           lista_palavras_unicas = list(set(lista_palavras))
           

#print(lista_palavras)
print(len(lista_palavras))
print(len(lista_palavras_unicas))
#print(por_palavra)





       

