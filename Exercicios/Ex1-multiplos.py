
#primeira versão
def multiplos(numero):
    lista = []
    for i in range(1, numero):
        if i % 3 == 0:
            lista.append(i)
        if i % 5 == 0:
            lista.append(i)
    teste = set(lista)
    return sum(teste)

print(multiplos(4)) 
    
#versão refatorada

def solution(number):
    lista = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 ==0:
            lista.append(i)
    return sum(lista)

#versao menor 
def solution(number):
    lista = [i for i in range(1,number) if i % 3 == 0 or i % 5 ==0]
    return sum(lista)
