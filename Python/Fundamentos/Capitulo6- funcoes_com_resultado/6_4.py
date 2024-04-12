def is_divisible(a, b):
    return a % b == 0

def is_potencia(a,b):
    if is_divisible(a,b) and is_divisible((a/b),b):
        return True
    else:
        return False
    
a = is_potencia(12,2)
print(a)