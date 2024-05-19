import string

#13.1
fin = open('texto.txt')
lista_palavras =[]
for line in fin:
    if line != '\n':
       line.strip()
       words = line.split()
       for word in words:
           word = word.translate(str.maketrans('','',string.punctuation))
           
           word = word.lower()
           
           lista_palavras.append(word)
           
#print(lista_palavras)



       

