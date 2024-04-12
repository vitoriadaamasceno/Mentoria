
import math


def retorno(x,y):
    if x>y:
        return 1
    elif x <y:
        return 0
    else:
        return -1
    
print(retorno(10,11))

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def area(radius):
    a = math.pi * radius**2
    return a
#Composicao
radius = distance(1,2, 4, 6)
result = area(radius)
print(result)

#Funções booleanas
""" def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False """
def is_divisible(x, y):
    return x % y == 0

if is_divisible(5, 2) == True:
    print('x is divisible by y')
else:
    print('x not is divisible by y')
