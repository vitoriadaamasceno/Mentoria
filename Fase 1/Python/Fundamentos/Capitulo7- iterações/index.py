""" def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:        # n é par
            n = n / 2
        else:                 # n é ímpar
            n = n * 3 + 1
            
#sequence(5)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
    
#print_n(2,6)


def print_n2(s,n):
    while n>0:
        print(s)
        n=n-1
        
#print_n2(4,6)

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!') """


""" def define():
    while True:
        string=input()
        if string=='done':
            break
        print(eval(string))
    print('FIM')

define()
 """
x= 3
a= 4
while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y
