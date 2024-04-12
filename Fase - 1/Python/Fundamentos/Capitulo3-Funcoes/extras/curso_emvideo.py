# funções para criar rotina
def mostra_linha(men):
    print('-'*40)
    print(men)
    print('-'*40)

mostra_linha("Sistema de alunos")

mostra_linha("Sistema de professores")


#2
def soma( a, b):
    print(a/b)

soma(b=3,a=9)


def contador (*num):
    print(num)
    print(len(num))

contador(1,2,3,4,5,6)
contador([1,2,3,4])


#3

valores =[3,4,8]

def dobra(lista):
    pos =0
    while pos < len(lista):
        lista[pos] *=2
        pos+=1
    print(lista)

     

dobra(valores)
#4 Desempacotar

def soma2(*valores):
    s = 0 
    for num in valores:
        s = s + num
    print(s)

soma2(2, 8, 1)
soma2(5, 8)
