fin = open('words.txt')



def construir_elemento(palavras):
    lista=[]
    for palavra in palavras:
        lista.append('x')
    print(len(lista))
    return lista
    

print(construir_elemento(fin))


