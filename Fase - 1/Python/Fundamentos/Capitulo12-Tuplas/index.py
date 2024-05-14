# as tuplas são muito parecidas com as listas. A diferença importante é que as tuplas são imutáveis.

t = 'a', 'b', 'c', 'd', 'e'
print(type(t))
t1 = ('a',)
print(type(t1))
print(t[0])
#substiuição de valores de uma tupla para outra tupla
t = ('A',) + t[1:]
print(t)
print('-------------------------------------------')
print((0, 1, 2) < (0, 3, 4))
print((0, 1, 2000000) < (0, 3, 4))
a=7
b=10
a,b = b,a
print(a)
print(b)

print('-------------------------------------------')
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)
t = divmod(10, 3) #divmod retorna uma tupla com o quociente e o resto da divisão
print(t)

quot, rem = divmod(7, 3)
print(quot)
print(rem)

def min_max(t):
    return min(t), max(t)

teste = min_max((1, 2, 3, 4, 5))
print(teste)

def printall(*args):
    print(args)
    
printall(1, 2.0, '3')

def sumall(*args):
    return sum(args)


total = sumall(1, 2, 3, 4, 5)
print(total)


s = 'abc'
t = [0, 1, 2]
zipado = zip(s, t)
print(zipado)

for pair in zip(s, t):
    print(pair) 
    
print('-------------------------------------------')

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)
    
    
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False
#retorna True se houver um match entre as tuplas
print(has_match((1, 2, 3), (7, 5, 3)))

#dicionarios e tuplas
d = {'a':0, 'b':1, 'c':2}
t = d.items() #transforma o dicionário em uma lista de tuplas
t
print(t)
for key, value in d.items():
     print((key, value))
     
tupla = (1, 2, 3, 4, 5)
print(reversed(tupla)) #erro, pois a tupla é imutável
