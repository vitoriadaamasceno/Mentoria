#tipos de divisões
minutes = 105
minutes = minutes / 60
print(minutes)

minutes = 105
hours = minutes // 60
hours
print(hours)

remainter = minutes%60
print(remainter)



#exp Booleanas
print(10==2*5)
x=12
y=2
x != y                # x não é igual a y
x > y                 # x é maior que y
x < y                 # x é menor que y
x >= y                # x é maior ou igual a y
x <= y                # x é menor ou igual a y

#Operadores lógicos
print(x> 0 and x <10)
print(not (x > y) )


#Execução condicional
if x > 0:
    print('x is positive')

if x < 0:
    pass          # A FAZER: lidar com valores negativos!

# Alternativa e aninhadas
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')
    else:
        print('caiu no else')

#Recursividade
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n("amo",2)

def recurse():
    recurse()
# Entrada de teclado
#text = input()
#print(text)
name = input('Wmahat...is your name?\n')